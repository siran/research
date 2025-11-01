#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PNPMD → PDF (Pandoc Markdown + pandoc-crossref; TOC after Abstract; spacing; anchor/link sugar)

Changes baked in:
- Intermediate file suffix is now .pandoc.md (not .pnp.md).
- [label]{#id} anchors are preserved and recorded as id→label for @id expansion.
- Plain prose {#id} (no colon) → []{#id}, skipping [label]{#id} and existing []{#id}.
- @id / [@id] →
    • [label](#id) if label was recorded from [label]{#id}
    • [@id](#id) if []{#id} or header {#id} exists
    • untouched otherwise
- [label](@id) / [label](@sec:id) normalized to [label](#...).
- @sec:id / [@sec:id] → \nameref{sec:id}.
- Bare #id in prose → [](#id) (not in code/headings/existing links).
- Crossref tokens (@…:…) and colon anchors ({#…:…}) left untouched otherwise.
- Reader: Pandoc Markdown (+tex_math_dollars), filter: pandoc-crossref.
- TOC inserted after Abstract if none exists; spacing normalized.
- autoSectionLabels options restored.

Usage:
  python renderpdf.py [--timeout N] [--omit-toc] [--omit-numbering] [--as-is] [file.md]
"""

import argparse, re, shutil, subprocess, sys, time, shlex
from pathlib import Path
from typing import Optional, Tuple, Set, Dict

# ---------- utils ----------
def discover_md_in_cwd() -> Path:
    cwd = Path.cwd()
    cands = [p for p in cwd.iterdir()
             if p.is_file() and p.suffix.lower()==".md"
             and not p.name.startswith(".")
             and not re.search(r"\.[A-Za-z0-9_-]+\.md$", p.name)]
    if len(cands)==1: return cands[0]
    if not cands: raise RuntimeError("No .md in current directory.")
    raise RuntimeError("Ambiguous .md in CWD:\n" + "\n".join(f" - {p.name}" for p in sorted(cands)))

def find_repo_root(start: Path) -> Path:
    try:
        top = subprocess.check_output(
            ["git","rev-parse","--show-toplevel"],
            cwd=start, text=True, stderr=subprocess.DEVNULL
        ).strip()
        if top: return Path(top)
    except Exception:
        pass
    cur = start
    while True:
        if (cur / "pnpmd.map").exists():
            return cur
        if cur.parent == cur: break
        cur = cur.parent
    raise FileNotFoundError("pnpmd.map not found in repo root or ancestors")

def _trim_ascii(s: str, *, left=True, right=True) -> str:
    if left:  s = re.sub(r'^[ \t]+', '', s)
    if right: s = re.sub(r'[ \ \t]+$', '', s)
    return s

def load_map(map_path: Path):
    if not map_path.exists():
        raise FileNotFoundError(f"Map file not found: {map_path}")
    out=[]
    for raw in map_path.read_text(encoding="utf-8").splitlines():
        if not raw or raw.lstrip().startswith("#") or "=" not in raw: continue
        lhs, rhs = raw.split("=", 1)
        lhs = _trim_ascii(lhs); rhs = _trim_ascii(rhs)
        if lhs == "": continue
        is_regex = lhs.startswith("/") and lhs.endswith("/") and len(lhs) >= 2
        out.append((lhs, rhs, is_regex))
    return out

def echo(cmd): print("+", cmd, flush=True)

def run_visible(cmd: str, *, timeout=0) -> int:
    echo(cmd)
    start = time.time()
    try:
        p = subprocess.Popen(cmd, shell=True)
        while True:
            if p.poll() is not None:
                return p.returncode
            if timeout and time.time() - start > timeout:
                try:
                    p.terminate(); time.sleep(0.5); p.kill()
                except Exception:
                    pass
                return 124
            time.sleep(0.1)
    except KeyboardInterrupt:
        try:
            p.kill()
        except Exception:
            pass
        return 130
    except Exception:
        return 1

# ---------- protect code ----------
_FENCE_RE = re.compile(r'(^|\n)(?P<f>```+|~~~+)[^\n]*\n.*?(\n(?P=f)[ \t]*\n|$)', re.DOTALL)
_INLINE_CODE_RE = re.compile(r'(?P<ticks>`+)(?P<body>[^`]*?)\1')
def _protect(text: str):
    blobs=[]
    def stash(m):
        i=len(blobs); blobs.append(m.group(0))
        return f"\u0000B{i}\u0000"
    text=_FENCE_RE.sub(stash, text)
    text=_INLINE_CODE_RE.sub(stash, text)
    return text, blobs
def _unprotect(text: str, blobs):
    return re.sub(r'\u0000B(\d+)\u0000', lambda mm: blobs[int(mm.group(1))], text)

# ---------- mapping (Unicode→TeX-ish replacements) ----------
def apply_mappings_safe(s: str, entries):
    prot, blobs = _protect(s)
    # regex rules first
    for lhs, rhs, is_regex in (e for e in entries if e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = re.sub(lhs[1:-1], rep, prot, flags=re.DOTALL)
    # then literal rules
    for lhs, rhs, is_regex in (e for e in entries if not e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = prot.replace(lhs, rep)
    return _unprotect(prot, blobs)

# ---------- parse leading % block ----------
_PERC_LINE = re.compile(r'^\s*%\s*(.*)\s*$')
def extract_percent_block(text: str):
    lines = text.splitlines()
    meta = {"title": None, "authors": [], "date": None}
    i = 0
    for j in range(min(3, len(lines))):
        m = _PERC_LINE.match(lines[j])
        if not m: break
        val = m.group(1).strip()
        if j == 0: meta["title"] = val or None
        elif j == 1:
            parts = [p.strip() for chunk in re.split(r'\band\b|,', val) for p in [chunk] if p.strip()]
            meta["authors"] = parts
        elif j == 2: meta["date"] = val or None
        i += 1
    raw_head = lines[:i]
    stripped = "\n".join(lines[i:]).lstrip("\n") if i else text
    return stripped, meta, raw_head

# ---------- headings / ids ----------
_HDR_RE = re.compile(r'^(?P<hash>#{1,6})\s+(?P<title>.+?)(?:\s+\{(?P<attrs>[^}]*)\})?\s*$')
_ATTR_ID_RE = re.compile(r'(?:^|\s)#([A-Za-z0-9_:-]+)(?=\s|$)')
_LINK_LABEL_RE = re.compile(r'\[([^\]]+)\]\([^)]+\)')
_FORMAT_MARKER_RE = re.compile(r'[*_~`]+')
def _auto_slug(title: str) -> str:
    t = _LINK_LABEL_RE.sub(r'\1', title)
    t = _FORMAT_MARKER_RE.sub('', t)
    t = t.lower()
    t = re.sub(r'[^0-9a-zA-Z _-]+', '', t)
    t = t.strip().replace(' ', '-')
    t = re.sub(r'-{2,}', '-', t).strip('-')
    return t or 'x'

def collect_all_ids(md: str) -> Set[str]:
    ids=set()
    for ln in md.splitlines():
        m=_HDR_RE.match(ln)
        if m:
            title=m.group('title')
            attrs=m.group('attrs') or ''
            for mm in _ATTR_ID_RE.finditer(attrs):
                ids.add(mm.group(1))
            ids.add(_auto_slug(title))
        # prose anchors {#id} too
        for mm in re.finditer(r'\{#([A-Za-z0-9_:-]+)\}', ln):
            ids.add(mm.group(1))
    return ids

# ---------- prose anchors ----------
_ATTR_BLOCK_RE = re.compile(r'\{#([A-Za-z0-9_:-]+)\}')
# [label]{#id}  (optional spaces before {#id})
_BRACKETED_LABEL_ANCHOR_RE = re.compile(r'\[([^\]]+?)\]\s*\{#([A-Za-z0-9_:-]+)\}')

def prose_anchors_and_labels(md: str) -> Tuple[str, Dict[str,str]]:
    """
    - Scan for [label]{#id} (no colon) and record id→label. Keep text unchanged.
    - Convert remaining prose {#id} (no colon) → []{#id}, but SKIP when it belongs to [label]{#id}.
    - Skip header lines.
    """
    out_lines=[]
    label_map: Dict[str,str] = {}

    for ln in md.splitlines():
        if _HDR_RE.match(ln):
            out_lines.append(ln); continue

        # Record labels from [label]{#id} without altering the line
        for m in _BRACKETED_LABEL_ANCHOR_RE.finditer(ln):
            label = m.group(1)
            pid   = m.group(2)
            if ":" in pid:  # crossref-style ids untouched
                continue
            label_map.setdefault(pid, label)

        # Convert remaining bare {#id} in prose → []{#id}  (no colon)
        def sub_attr(m):
            pid = m.group(1)
            if ":" in pid:
                return m.group(0)
            start = m.start()
            prefix = ln[:start]
            # already "[] {#id}" or "[]{#id}"?
            if re.search(r'\[\]\s*$', prefix):
                return m.group(0)
            # is part of a [label]{#id} pattern (possibly with spaces)?
            if re.search(r'\]\s*$', prefix):
                return m.group(0)
            return f'[]{{#{pid}}}'
        ln2 = _ATTR_BLOCK_RE.sub(sub_attr, ln)
        out_lines.append(ln2)

    return "\n".join(out_lines), label_map

# ---------- normalize [label](@id) / [label](@sec:id) → [label](#id / #sec:id) ----------
_DEST_NORM_RE = re.compile(r'\]\(\s*@(?:(sec|fig|eq|tbl):)?([A-Za-z0-9_-]+)\s*\)')
def normalize_link_destinations(md: str) -> str:
    def repl(m):
        kind = m.group(1)
        ident = m.group(2)
        return f'](#{kind+":"+ident if kind else ident})'
    return _DEST_NORM_RE.sub(repl, md)

# ---------- @id sugar (uses label_map, span_ids, header_ids) ----------
_AT_UNBRACKETED = re.compile(r'(?<![A-Za-z0-9._%+-])@(?P<id>[A-Za-z0-9_-]+)\b')
_AT_BRACKETED   = re.compile(r'\[\s*@(?P<id>[A-Za-z0-9_-]+)\s*\]')
_EMPTY_SPAN_ANCHOR_RE = re.compile(r'\[\]\{#([A-Za-z0-9_-]+)\}')

def rewrite_at_tokens(md: str, *, label_map: Dict[str,str], span_ids: Set[str], header_ids: Set[str]) -> str:
    """
    @id / [@id] →
      - [label](#id)  if id in label_map
      - [@id](#id)    if id in span_ids or header_ids
      - untouched     otherwise
    (Colon tokens are handled separately.)
    """
    prot, blobs = _protect(md)
    outs=[]
    def keep(s: str) -> str:
        i=len(outs); outs.append(s)
        return f"\u0000L{i}\u0000"

    def make_link(ident: str, bracketed: bool) -> str:
        # skip 'sec:' here; handled by dedicated pass for \nameref
        if ":" in ident:
            return f'@{ident}' if not bracketed else f'[@{ident}]'
        if ident in label_map:
            return f'[{label_map[ident]}](#{ident})'
        if ident in span_ids or ident in header_ids:
            return f'[@{ident}](#{ident})'
        return f'@{ident}' if not bracketed else f'[@{ident}]'

    prot = _AT_BRACKETED.sub(lambda m: keep(make_link(m.group("id"), True)), prot)
    prot = _AT_UNBRACKETED.sub(lambda m: keep(make_link(m.group("id"), False)), prot)

    prot = re.sub(r'\u0000L(\d+)\u0000', lambda mm: outs[int(mm.group(1))], prot)
    return _unprotect(prot, blobs)

# ---------- NEW: @sec:id (and [@sec:id]) → \nameref{sec:id} ----------
_SEC_UNBR = re.compile(r'(?<![A-Za-z0-9._%+-])@sec:([A-Za-z0-9_-]+)\b')
_SEC_BRKT = re.compile(r'\[\s*@sec:([A-Za-z0-9_-]+)\s*\]')

def atsec_to_nameref(md: str) -> str:
    prot, blobs = _protect(md)
    prot = _SEC_BRKT.sub(lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot)
    prot = _SEC_UNBR.sub(lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot)
    return _unprotect(prot, blobs)

# ---------- bare #id → [](#id) ----------
_BARE_HASH_RE = re.compile(r'(?<![#A-Za-z0-9_{(])#([A-Za-z0-9_:-]+)\b(?!\()')
def rewrite_hash_anchors(md: str) -> str:
    prot, blobs = _protect(md)
    def repl_line(ln: str) -> str:
        if _HDR_RE.match(ln): return ln
        return _BARE_HASH_RE.sub(lambda m: f'[](#{m.group(1)})', ln)
    new_lines = [repl_line(ln) for ln in prot.splitlines()]
    prot2 = "\n".join(new_lines)
    return _unprotect(prot2, blobs)

# ---------- TOC handling ----------
_TOC_MARK_RE = re.compile(r'^\s*\[\[TOC\]\]\s*$', re.MULTILINE)
def insert_toc_after_abstract_content(md: str) -> str:
    if _TOC_MARK_RE.search(md): return md
    lines = md.splitlines()
    abs_idx = None; lvl = None
    for i, ln in enumerate(lines):
        m=_HDR_RE.match(ln)
        if not m: continue
        title=m.group('title').strip()
        if title.lower().startswith('abstract'):
            abs_idx=i; lvl=len(m.group('hash')); break
    if abs_idx is None: return md
    end=len(lines)
    for j in range(abs_idx+1, len(lines)):
        m=_HDR_RE.match(lines[j])
        if m and len(m.group('hash'))<=lvl:
            end=j; break
    lines.insert(end, ""); lines.insert(end+1, "\n[[TOC]]\n"); lines.insert(end+2, "")
    return "\n".join(lines)

def replace_toc_marker(md: str) -> Tuple[str,bool]:
    if _TOC_MARK_RE.search(md):
        return _TOC_MARK_RE.sub(r'\n\\tableofcontents\n', md), True
    return md, False

# ---------- spacing ----------
def normalize_heading_spacing(md: str) -> str:
    prot, blobs = _protect(md)
    lines = prot.splitlines()
    out=[]
    for i, ln in enumerate(lines):
        if _HDR_RE.match(ln):
            if len(out)>=1 and out[-1].strip()!="": out.append("")
            if len(out)>=2 and out[-2].strip()!="": out.append("")
            out.append(ln)
            if i+1<len(lines) and lines[i+1].strip()!="": out.append("")
        else:
            out.append(ln)
    return _unprotect("\n".join(out), blobs)

# ---------- pandoc driver ----------
def renderpdf(path: str|None=None, *, timeout=0, omit_toc=False, omit_numbering=False, as_is: bool=False) -> Path:
    src = Path(path) if path else discover_md_in_cwd()
    if not src.exists(): raise FileNotFoundError(str(src))

    # ---------- AS-IS path: no preprocessing ----------
    if as_is:
        tmpdir = Path("/tmp")
        in_tmp  = tmpdir / src.name
        out_tmp = tmpdir / src.with_suffix(".pdf").name
        shutil.copy2(src, in_tmp)

        reader = "markdown+tex_math_dollars"
        toc_flag = "" if omit_toc else "--toc "
        numbering_flag = "" if omit_numbering else "--number-sections "

        cmd=(
            f"docker run --rm "
            f"--mount type=bind,source=\"{tmpdir}\",target=/data -w /data pandoc/extra "
            f"--standalone {toc_flag}{numbering_flag}--toc-depth=2 "
            f"--filter pandoc-crossref "
            f"-f {reader} "
            f"'{in_tmp.name}' -o '{out_tmp.name}'"
        )
        rc=run_visible(cmd,timeout=timeout)
        if rc!=0: raise RuntimeError(f"Docker pandoc failed (rc={rc}).")

        final_pdf=src.with_suffix(".pdf")
        shutil.copy2(out_tmp,final_pdf)
        print(f"✅ Wrote {final_pdf}")
        return final_pdf.resolve()

    # ---------- normal (preprocessed) path ----------
    repo = find_repo_root(src.parent)
    entries = load_map(repo / "pnpmd.map")
    print(f"Using map: {repo/'pnpmd.map'}  (rules={len(entries)})")

    raw = src.read_text(encoding="utf-8").replace("\r\n","\n")
    mapped = apply_mappings_safe(raw, entries)

    stripped, meta, raw_head = extract_percent_block(mapped)

    # Gather header & inline IDs early (for fallback @id → [@id](#id))
    header_and_inline_ids = collect_all_ids(stripped)

    # 1) Record labels from [label]{#id}; convert prose {#id} → []{#id}
    body, label_map = prose_anchors_and_labels(stripped)

    # 2) Normalize [label](@id) / [label](@sec:id)
    body = normalize_link_destinations(body)

    # 3) @id / [@id] → links using label_map or existing anchors/headers
    span_ids = set(_EMPTY_SPAN_ANCHOR_RE.findall(body))  # after step 1
    body = rewrite_at_tokens(body, label_map=label_map, span_ids=span_ids, header_ids=header_and_inline_ids)

    # 3.5) Convert @sec:id and [@sec:id] → \nameref{sec:id}
    body = atsec_to_nameref(body)

    # 4) bare #id → [](#id)
    body = rewrite_hash_anchors(body)

    # 5) spacing around headings
    body = normalize_heading_spacing(body)

    # write .pandoc.md
    final_pandoc_md = src.with_suffix(".pandoc.md")
    keep_head = "\n".join(raw_head) + ("\n\n" if raw_head else "")
    final_pandoc_md.write_text(keep_head + body, encoding="utf-8")

    # TOC controls
    body2 = body
    has_toc_marker = False
    if not omit_toc:
        body2 = insert_toc_after_abstract_content(body2)
        body2, has_toc_marker = replace_toc_marker(body2)

    # temp files for docker pandoc
    tmpdir = Path("/tmp")
    in_tmp  = tmpdir / final_pandoc_md.name
    out_tmp = tmpdir / src.with_suffix(".pdf").name

    # IMPORTANT: feed Pandoc the TOC-processed content (body2) when applicable
    text_for_pandoc = keep_head + (body2 if not omit_toc else body)
    in_tmp.write_text(text_for_pandoc, encoding="utf-8")
    # shutil.copy2(final_pandoc_md, in_tmp)

    # metadata args (including approved autoSectionLabels flags)
    meta_args=[]
    if meta.get("title"): meta_args.append(f"-M title={shlex.quote(meta['title'])}")
    for a in meta.get("authors", []): meta_args.append(f"-M author={shlex.quote(a)}")
    if meta.get("date"): meta_args.append(f"-M date={shlex.quote(meta['date'])}")
    meta_args.append("-M autoSectionLabels=true")
    meta_args.append("-M autoSectionLabelsDepth=6")
    meta_args.append("-M toc-title=Table of Contents")

    # heading level shift
    def min_heading_level(md: str) -> Optional[int]:
        lvl=None
        for ln in md.splitlines():
            m=_HDR_RE.match(ln)
            if not m: continue
            n=len(m.group('hash'))
            lvl=n if lvl is None else min(lvl, n)
        return lvl
    shift=0
    mhl=min_heading_level(body2)
    if mhl and mhl>1: shift=1-mhl
    shift_arg=f"--shift-heading-level-by={shift} " if shift!=0 else ""

    # Pandoc (Markdown reader + pandoc-crossref)
    reader = "markdown+tex_math_dollars+raw_tex"
    toc_flag = "" if (has_toc_marker or omit_toc) else "--toc "
    numbering_flag = "" if omit_numbering else "--number-sections "

    cmd=(
        f"docker run --rm "
        f"--mount type=bind,source=\"{tmpdir}\",target=/data -w /data pandoc/extra "
        f"--standalone {toc_flag}{numbering_flag}--toc-depth=2 "
        f"{shift_arg}"
        f"{' '.join(meta_args)} "
        f"--filter pandoc-crossref "
        f"-f {reader} "
        f"'{in_tmp.name}' -o '{out_tmp.name}'"
    )
    rc=run_visible(cmd,timeout=timeout)
    if rc!=0: raise RuntimeError(f"Docker pandoc failed (rc={rc}).")

    final_pdf=src.with_suffix(".pdf")
    shutil.copy2(out_tmp,final_pdf)
    print(f"✅ Wrote {final_pdf}, {final_pandoc_md}")
    return final_pdf.resolve()

# ---------- CLI ----------
def main(argv=None):
    ap=argparse.ArgumentParser(description="PNPMD → PDF (Markdown + crossref; TOC after Abstract; spacing; link sugar).")
    ap.add_argument("file",nargs="?",help="Markdown file; if omitted, exactly one .md in CWD is required.")
    ap.add_argument("--timeout",type=int,default=0,help="Timeout seconds (0=no timeout).")
    ap.add_argument("--omit-toc",action="store_true",
        help="Do not include table of contents in the final PDF (disables [[TOC]] insertion and --toc).")
    ap.add_argument("--omit-numbering",action="store_true",
        help="Disable section numbering in the final PDF.")
    ap.add_argument("--as-is",action="store_true",
        help="Bypass all preprocessing and pass the original Markdown directly to Pandoc.")
    args=argparse.Namespace()  # silence mypy
    args=ap.parse_args(argv)
    try:
        renderpdf(args.file, timeout=args.timeout,
                  omit_toc=args.omit_toc,
                  omit_numbering=args.omit_numbering,
                  as_is=args.as_is)
    except Exception as e:
        print(f"❌ {e}",file=sys.stderr); sys.exit(1)

if __name__=="__main__":
    main()
