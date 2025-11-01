#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PNPMD → PDF preprocessor and renderer

OVERVIEW
--------
This tool preprocesses a PNPMD Markdown source, then renders a PDF using
Pandoc + pandoc-crossref in a Docker container. The preprocessing phase applies
readability-preserving transformations that standardize anchors, expand sugar
for references, normalize spacing, and (optionally) insert a TOC after the
Keywords section. The renderer then compiles the processed Markdown to PDF.

WHAT THIS SCRIPT DOES (PIPELINE)
--------------------------------
1) Repository map replacements
   - Loads `pnpmd.map` from the repository root and applies Unicode→TeX(ish)
     substitutions safely (code blocks, inline code, and math are protected).
   - Supports both literal and regex rules; regex rules are applied first.
   - If a replacement starts with a backslash (e.g., `\alpha`), it is wrapped
     in `$...$` to become math mode.

2) Header extraction (leading `%` block)
   - Reads up to 3 leading `% ...` lines as title, authors, and date.
   - These are passed as Pandoc metadata unless explicitly overridden later.

3) Anchor and link sugar
   - Records labels from `[label]{#id}` (no colon) for later `@id` expansion.
   - Converts plain prose `{#id}` (no colon) → `[]{#id}` (headers untouched;
     **content inside code or math is left as-is**).
   - Normalizes `[label](@id)` / `[label](@sec:id)` → `[label](#id)` / `(#sec:id)`
     **only outside code and math**.
   - Rewrites `@id` / `[@id]` to links:
       • `[label](#id)` if label was recorded from `[label]{#id}`
       • `[@id](#id)`   if a span/header anchor exists
       • left untouched otherwise
   - Rewrites `@sec:id` and `[@sec:id]` to `\nameref{sec:id}` so crossref yields
     stable name references without interfering with Pandoc link resolution.
   - Converts bare `#id` in prose to `[](#id)` for consistency (not inside code,
     headings, or existing links).
   - Leaves crossref tokens like `@fig:...` and colon-anchors `{#eq:...}` intact.

4) Spacing normalization
   - Ensures two blank lines before headings and one after, improving readability
     of the raw Markdown without altering content.

5) TOC handling (optional)
   - If no `[[TOC]]` marker exists and `--omit-toc` is not set, inserts a TOC
     immediately after the **Keywords** section.
   - Replaces `[[TOC]]` with `\tableofcontents` for LaTeX output.

6) Safe rendering via Docker
   - Writes preprocessed text to a temporary directory with safe filenames.
   - Computes a heading shift that never creates level-0 headers.
   - Invokes `pandoc/extra` with:
       • `--standalone`, section numbering (unless `--omit-numbering`)
       • `--toc` (unless `--omit-toc` or an explicit TOC is injected)
       • `--toc-depth=2`
       • `-M autoSectionLabels=true`
       • `-M autoSectionLabelsDepth=6`
       • `-M autoSectionLabelsPrefix=sec:`   (restores classic @sec: targets)
       • `-M toc-title=Table of Contents`
       • `--filter pandoc-crossref`
       • `-f markdown+tex_math_dollars+raw_tex`
   - Copies the resulting PDF next to the source Markdown.
   - Also writes a `.pandoc.md` alongside the source for inspection.

INPUT / OUTPUT
--------------
Input : A `.md` file written in PNPMD style.
Output: A `.pdf` with the same basename, and a `.pandoc.md` (preprocessed source).

USAGE
-----
  python renderpdf.py [--timeout N] [--omit-toc] [--omit-numbering] [--as-is] [file.md]

OPTIONS
-------
--timeout N        Kill the Docker run after N seconds (0 = no timeout).
--omit-toc         Do not include a Table of Contents in the final PDF.
--omit-numbering   Do not number sections.
--as-is            Bypass preprocessing; pass the original Markdown to Pandoc.

EXAMPLES
--------
  # Standard preprocess + render
  python renderpdf.py paper.md

  # Render "as is" (no preprocessing), with section numbering and TOC
  python renderpdf.py --as-is paper.md

REQUIREMENTS
------------
- Docker with `pandoc/extra` image available.
- `pandoc-crossref` present inside the image (provided by `pandoc/extra`).
- A `pnpmd.map` file at the repo root (or ancestor) when preprocessing.

EXIT CODES
----------
0   Success
124 Timeout hit (Docker terminated)
130 Interrupted (Ctrl-C)
>0  Other failure (printed message explains the error)

DESIGN NOTES
------------
- All transformations attempt to be idempotent over clean PNPMD sources.
- Code fences, inline code, and math (inline `$...$` and display `$$...$$`)
  are protected during transformations.
- Heading shift is computed to avoid producing level-0 headings, which would
  break auto section labeling and cross-references.
"""

import argparse, re, shutil, subprocess, sys, time, shlex, tempfile, os
from pathlib import Path
from typing import Optional, Tuple, Set, Dict

# ---------- Utility helpers ----------
def discover_md_in_cwd() -> Path:
    """
    Return the single .md file in CWD if exactly one exists; otherwise raise.
    Excludes hidden files and files like *.something.md (treated as derived).
    """
    cwd = Path.cwd()
    cands = [p for p in cwd.iterdir()
             if p.is_file() and p.suffix.lower()==".md"
             and not p.name.startswith(".")
             and not re.search(r"\.[A-Za-z0-9_-]+\.md$", p.name)]
    if len(cands)==1: return cands[0]
    if not cands: raise RuntimeError("No .md in current directory.")
    raise RuntimeError("Ambiguous .md in CWD:\n" + "\n".join(f" - {p.name}" for p in sorted(cands)))

def find_repo_root(start: Path) -> Path:
    """
    Resolve repository root to locate pnpmd.map:
    - Prefer `git rev-parse --show-toplevel` if available.
    - Fallback: walk up directories looking for `pnpmd.map`.
    """
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
    """Trim ASCII spaces/tabs on left/right sides."""
    if left:  s = re.sub(r'^[ \t]+', '', s)
    if right: s = re.sub(r'[ \ \t]+$', '', s)
    return s

def load_map(map_path: Path):
    """
    Load substitution rules from pnpmd.map.
    Each non-comment, non-empty line must contain 'lhs=rhs'.
    Regex rules are wrapped with slashes: /.../ = replacement
    """
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

def echo(cmd_list):
    """Pretty-print the exact command we will execute (shell-quote each arg)."""
    print("+", " ".join(shlex.quote(x) for x in cmd_list), flush=True)

def run_visible(cmd_list, *, timeout=0) -> int:
    """
    Run a process visibly. Poll for completion; on timeout, terminate.
    Return the process return code, or 124 on timeout, 130 on Ctrl-C.
    """
    echo(cmd_list)
    start = time.time()
    try:
        p = subprocess.Popen(cmd_list)
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

# ---------- Protection of code blocks, inline code, and math ----------
# These ensure replacements/sugar never touch code or math.
_FENCE_RE = re.compile(r'(^|\n)(?P<f>```+|~~~+)[^\n]*\n.*?(\n(?P=f)[ \t]*\n|$)', re.DOTALL)
_INLINE_CODE_RE = re.compile(r'(?P<ticks>`+)(?P<body>[^`]*?)\1')
# Protect display math $$...$$ (multiline)
_MATH_BLOCK_RE = re.compile(r'(^|\n)\$\$[\s\S]*?\$\$(?=\s*(\n|$))', re.MULTILINE)
# Protect inline math $...$ (naive but effective; ignores $$)
_INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)(?:\\\$|[^$])+\$(?!\$)')

def _protect(text: str):
    """Replace code/math regions with sentinels, returning (protected_text, blobs)."""
    blobs=[]
    def stash(m):
        i=len(blobs); blobs.append(m.group(0))
        return f"\u0000B{i}\u0000"
    # Order: fences → inline code → block math → inline math
    text=_FENCE_RE.sub(stash, text)
    text=_INLINE_CODE_RE.sub(stash, text)
    text=_MATH_BLOCK_RE.sub(stash, text)
    text=_INLINE_MATH_RE.sub(stash, text)
    return text, blobs

def _unprotect(text: str, blobs):
    """Restore protected regions from sentinels."""
    return re.sub(r'\u0000B(\d+)\u0000', lambda mm: blobs[int(mm.group(1))], text)

# ---------- Mapping (Unicode → TeX-ish) ----------
def apply_mappings_safe(s: str, entries):
    """
    Apply map entries in two passes: regex first, then literal.
    If RHS begins with backslash, wrap in $...$ to enter math mode.
    Code/math are protected.
    """
    prot, blobs = _protect(s)
    for lhs, rhs, is_regex in (e for e in entries if e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = re.sub(lhs[1:-1], rep, prot, flags=re.DOTALL)
    for lhs, rhs, is_regex in (e for e in entries if not e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = prot.replace(lhs, rep)
    return _unprotect(prot, blobs)

# ---------- Parse leading `%` header block ----------
_PERC_LINE = re.compile(r'^\s*%\s*(.*)\s*$')

def extract_percent_block(text: str):
    """
    Extract up to three leading lines starting with `%` as (title, authors, date).
    Return (body_without_header, meta_dict, raw_header_lines).
    """
    lines = text.splitlines()
    meta = {"title": None, "authors": [], "date": None}
    i = 0
    for j in range(min(3, len(lines))):
        m = _PERC_LINE.match(lines[j])
        if not m: break
        val = m.group(1).strip()
        if j == 0: meta["title"] = val or None
        elif j == 1:
            # Split on "and" or comma; keep simple and robust.
            parts = [p.strip() for chunk in re.split(r'\band\b|,', val) for p in [chunk] if p.strip()]
            meta["authors"] = parts
        elif j == 2: meta["date"] = val or None
        i += 1
    raw_head = lines[:i]
    stripped = "\n".join(lines[i:]).lstrip("\n") if i else text
    return stripped, meta, raw_head

# ---------- Headings / IDs ----------
_HDR_RE = re.compile(r'^(?P<hash>#{1,6})\s+(?P<title>.+?)(?:\s+\{(?P<attrs>[^}]*)\})?\s*$')
_ATTR_ID_RE = re.compile(r'(?:^|\s)#([A-Za-z0-9_:-]+)(?=\s|$)')
_LINK_LABEL_RE = re.compile(r'\[([^\]]+)\]\([^)]+\)')
_FORMAT_MARKER_RE = re.compile(r'[*_~`]+')

def _auto_slug(title: str) -> str:
    """Compute a Pandoc-like slug for a heading title (approximate)."""
    t = _LINK_LABEL_RE.sub(r'\1', title)
    t = _FORMAT_MARKER_RE.sub('', t)
    t = t.lower()
    t = re.sub(r'[^0-9a-zA-Z _-]+', '', t)
    t = t.strip().replace(' ', '-')
    t = re.sub(r'-{2,}', '-', t).strip('-')
    return t or 'x'

def collect_all_ids(md: str) -> Set[str]:
    """Collect slugs for all headings and explicit prose anchors `{#id}`."""
    ids=set()
    for ln in md.splitlines():
        m=_HDR_RE.match(ln)
        if m:
            title=m.group('title')
            attrs=m.group('attrs') or ''
            for mm in _ATTR_ID_RE.finditer(attrs):
                ids.add(mm.group(1))
            ids.add(_auto_slug(title))
        for mm in re.finditer(r'\{#([A-Za-z0-9_:-]+)\}', ln):
            ids.add(mm.group(1))
    return ids

# ---------- Prose anchors and label capture ----------
_ATTR_BLOCK_RE = re.compile(r'\{#([A-Za-z0-9_:-]+)\}')
_BRACKETED_LABEL_ANCHOR_RE = re.compile(r'\[([^\]]+?)\]\s*\{#([A-Za-z0-9_:-]+)\}')

def prose_anchors_and_labels(md: str) -> Tuple[str, Dict[str,str]]:
    """
    - Record labels from `[label]{#id}` (no colon in id); do not modify the text.
    - Convert remaining bare `{#id}` (no colon) in prose → `[]{#id}`.
    - Skip header lines entirely.
    - **Respect protection**: no changes inside code blocks, inline code, or math.
    """
    prot, blobs = _protect(md)

    out_lines=[]
    label_map: Dict[str,str] = {}

    for ln in prot.splitlines():
        if _HDR_RE.match(ln):
            out_lines.append(ln); continue

        # Capture labels from "[label]{#id}" without colon; ignore crossref ids.
        for m in _BRACKETED_LABEL_ANCHOR_RE.finditer(ln):
            label = m.group(1)
            pid   = m.group(2)
            if ":" in pid:
                continue
            label_map.setdefault(pid, label)

        # Convert plain prose "{#id}" → "[]{#id}" unless it's already tied to a label.
        def sub_attr(m):
            pid = m.group(1)
            if ":" in pid:
                return m.group(0)
            start = m.start()
            prefix = ln[:start]
            if re.search(r'\[\]\s*$', prefix):  # already []{#id}
                return m.group(0)
            if re.search(r'\]\s*$', prefix):    # part of [label]{#id}
                return m.group(0)
            return f'[]{{#{pid}}}'
        ln2 = _ATTR_BLOCK_RE.sub(sub_attr, ln)
        out_lines.append(ln2)

    result = "\n".join(out_lines)
    return _unprotect(result, blobs), label_map

# ---------- Normalize [label](@id) / [label](@sec:id) destinations ----------
_DEST_NORM_RE = re.compile(r'\]\(\s*@(?:(sec|fig|eq|tbl):)?([A-Za-z0-9_-]+)\s*\)')
def normalize_link_destinations(md: str) -> str:
    """
    Turn [label](@id) → [label](#id) and [label](@sec:id) → [label](#sec:id),
    but NEVER inside code fences, inline code, or math.
    """
    prot, blobs = _protect(md)
    def repl(m):
        kind = m.group(1)
        ident = m.group(2)
        return f'](#{kind+":"+ident if kind else ident})'
    prot = _DEST_NORM_RE.sub(repl, prot)
    return _unprotect(prot, blobs)

# ---------- Expand @id tokens ----------
_AT_UNBRACKETED = re.compile(r'(?<![A-Za-z0-9._%+-])@(?P<id>[A-Za-z0-9_-]+)\b')
_AT_BRACKETED   = re.compile(r'\[\s*@(?P<id>[A-Za-z0-9_-]+)\s*\]')
_EMPTY_SPAN_ANCHOR_RE = re.compile(r'\[\]\{#([A-Za-z0-9_-]+)\}')

def rewrite_at_tokens(md: str, *, label_map: Dict[str,str], span_ids: Set[str], header_ids: Set[str]) -> str:
    """
    Expand:
      @id      → [label](#id) if labeled; [@id](#id) if anchor exists; else leave as-is
      [@id]    → same logic, preserving bracketed style
    Crossref tokens with colon (e.g., sec:...) are not handled here.
    """
    prot, blobs = _protect(md)
    outs=[]
    def keep(s: str) -> str:
        i=len(outs); outs.append(s)
        return f"\u0000L{i}\u0000"

    def make_link(ident: str, bracketed: bool) -> str:
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

# ---------- Convert @sec:id and [@sec:id] to \nameref{sec:id} ----------
_SEC_UNBR = re.compile(r'(?<![A-Za-z0-9._%+-])@sec:([A-Za-z0-9_-]+)\b')
_SEC_BRKT = re.compile(r'\[\s*@sec:([A-Za-z0-9_-]+)\s*\]')

def atsec_to_nameref(md: str) -> str:
    """Turn @sec:id (and bracketed form) into LaTeX \\nameref{sec:id}."""
    prot, blobs = _protect(md)
    prot = _SEC_BRKT.sub(lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot)
    prot = _SEC_UNBR.sub(lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot)
    return _unprotect(prot, blobs)

# ---------- Bare #id in prose → [](#id) ----------
_BARE_HASH_RE = re.compile(r'(?<![#A-Za-z0-9_{(])#([A-Za-z0-9_:-]+)\b(?!\()')
def rewrite_hash_anchors(md: str) -> str:
    """Convert bare '#id' references in prose to link spans '[](#id)'."""
    prot, blobs = _protect(md)
    def repl_line(ln: str) -> str:
        if _HDR_RE.match(ln): return ln
        return _BARE_HASH_RE.sub(lambda m: f'[](#{m.group(1)})', ln)
    new_lines = [repl_line(ln) for ln in prot.splitlines()]
    prot2 = "\n".join(new_lines)
    return _unprotect(prot2, blobs)

# ---------- TOC handling ----------
_TOC_MARK_RE = re.compile(r'^\s*\[\[TOC\]\]\s*$', re.MULTILINE)

def insert_toc_after_keywords_content(md: str) -> str:
    """
    If no [[TOC]] exists, insert it immediately after the Keywords section
    (same or higher-level next heading marks the end of that section).
    """
    if _TOC_MARK_RE.search(md): return md
    lines = md.splitlines()
    start_idx = None; lvl = None
    for i, ln in enumerate(lines):
        m=_HDR_RE.match(ln)
        if not m: continue
        title=m.group('title').strip()
        if title.lower().startswith('keywords'):
            start_idx=i; lvl=len(m.group('hash')); break
    if start_idx is None: return md
    end=len(lines)
    for j in range(start_idx+1, len(lines)):
        m=_HDR_RE.match(lines[j])
        if m and len(m.group('hash'))<=lvl:
            end=j; break
    # Insert on a clean paragraph boundary.
    lines.insert(end, ""); lines.insert(end+1, "\n[[TOC]]\n"); lines.insert(end+2, "")
    return "\n".join(lines)

def replace_toc_marker(md: str) -> Tuple[str,bool]:
    """Replace [[TOC]] markers with LaTeX \\tableofcontents; return (text, replaced?)."""
    if _TOC_MARK_RE.search(md):
        return _TOC_MARK_RE.sub(r'\n\\tableofcontents\n', md), True
    return md, False

# ---------- Spacing normalization ----------
def normalize_heading_spacing(md: str) -> str:
    """
    Ensure two blank lines before each heading and one blank line after,
    without touching code blocks or math (protected earlier).
    """
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

# ---------- Pandoc driver ----------
def renderpdf(path: str|None=None, *, timeout=0, omit_toc=False, omit_numbering=False, as_is: bool=False) -> Path:
    """
    Preprocess PNPMD and render PDF via Dockerized Pandoc.
    Returns the absolute path to the final PDF.
    """
    src = Path(path) if path else discover_md_in_cwd()
    if not src.exists(): raise FileNotFoundError(str(src))

    # ---------- AS-IS path: pass original Markdown directly to Pandoc ----------
    if as_is:
        tmpdir = Path(tempfile.mkdtemp(prefix="pnpmd_"))
        in_tmp  = tmpdir / "in.md"
        out_tmp = tmpdir / "out.pdf"
        in_tmp.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

        reader = "markdown+tex_math_dollars"
        toc_flag = [] if omit_toc else ["--toc"]
        numbering_flag = [] if omit_numbering else ["--number-sections"]

        cmd = (["docker","run","--rm",
                "--mount", f"type=bind,source={str(tmpdir)},target=/data",
                "-w","/data","pandoc/extra",
                "--standalone", *toc_flag, *numbering_flag, "--toc-depth=2",
                "--filter","pandoc-crossref",
                "-f", reader, "in.md", "-o", "out.pdf"])
        rc=run_visible(cmd,timeout=timeout)
        if rc!=0: raise RuntimeError(f"Docker pandoc failed (rc={rc}).")

        final_pdf=src.with_suffix(".pdf")
        shutil.copy2(out_tmp,final_pdf)
        print(f"✅ Wrote {final_pdf}")
        return final_pdf.resolve()

    # ---------- Normal (preprocessed) path ----------
    repo = find_repo_root(src.parent)
    entries = load_map(repo / "pnpmd.map")
    print(f"Using map: {repo/'pnpmd.map'}  (rules={len(entries)})")

    raw = src.read_text(encoding="utf-8").replace("\r\n","\n")

    # 1) Apply repository mappings safely (code/math-protected).
    mapped = apply_mappings_safe(raw, entries)

    # 2) Extract leading % header (if any).
    stripped, meta, raw_head = extract_percent_block(mapped)

    # Gather known anchors from headers/prose for @id expansion fallback.
    header_and_inline_ids = collect_all_ids(stripped)

    # 3) Anchor/label sugar & link normalization (code/math-protected internally).
    body, label_map = prose_anchors_and_labels(stripped)
    body = normalize_link_destinations(body)
    span_ids = set(_EMPTY_SPAN_ANCHOR_RE.findall(body))  # after step 3a
    body = rewrite_at_tokens(body, label_map=label_map, span_ids=span_ids, header_ids=header_and_inline_ids)
    body = atsec_to_nameref(body)
    body = rewrite_hash_anchors(body)

    # 4) Spacing normalization.
    body = normalize_heading_spacing(body)

    # Write checkpointed .pandoc.md for inspection.
    final_pandoc_md = src.with_suffix(".pandoc.md")
    keep_head = "\n".join(raw_head) + ("\n\n" if raw_head else "")
    final_pandoc_md.write_text(keep_head + body, encoding="utf-8")

    # 5) TOC insertion/replacement — now after Keywords.
    body2 = body
    has_toc_marker = False
    if not omit_toc:
        body2 = insert_toc_after_keywords_content(body2)
        body2, has_toc_marker = replace_toc_marker(body2)

    # Use a temp workspace with safe filenames (no quoting pitfalls).
    tmpdir = Path(tempfile.mkdtemp(prefix="pnpmd_"))
    in_tmp  = tmpdir / "in.md"
    out_tmp = tmpdir / "out.pdf"
    text_for_pandoc = keep_head + (body2 if not omit_toc else body)
    in_tmp.write_text(text_for_pandoc, encoding="utf-8")

    # Pandoc metadata args (include autoSectionLabelsPrefix=sec: to restore @sec:*)
    meta_args=[]
    if meta.get("title"): meta_args += ["-M", f"title={meta['title']}"]
    for a in meta.get("authors", []): meta_args += ["-M", f"author={a}"]
    if meta.get("date"): meta_args += ["-M", f"date={meta['date']}"]
    meta_args += ["-M","autoSectionLabels=true",
                  "-M","autoSectionLabelsDepth=6",
                  "-M","autoSectionLabelsPrefix=sec:",
                  "-M","toc-title=Table of Contents"]

    # Compute safe heading shift (never create level-0 headers).
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
    if mhl and mhl>1:
        shift = 1 - mhl  # negative: raise headings so minimum becomes H1
    else:
        shift = 0
    shift_args = ["--shift-heading-level-by", str(shift)] if shift != 0 else []

    reader = "markdown+tex_math_dollars+raw_tex"
    toc_flag = [] if (has_toc_marker or omit_toc) else ["--toc"]
    numbering_flag = [] if omit_numbering else ["--number-sections"]

    # Final Docker invocation
    cmd = (["docker","run","--rm",
            "--mount", f"type=bind,source={str(tmpdir)},target=/data",
            "-w","/data","pandoc/extra",
            "--standalone", *toc_flag, *numbering_flag, "--toc-depth=2",
            *shift_args,
            *meta_args,
            "--filter","pandoc-crossref",
            "-f", reader, "in.md", "-o", "out.pdf"])
    rc=run_visible(cmd,timeout=timeout)
    if rc!=0: raise RuntimeError(f"Docker pandoc failed (rc={rc}).")

    final_pdf=src.with_suffix(".pdf")
    shutil.copy2(out_tmp,final_pdf)
    print(f"✅ Wrote {final_pdf}, {final_pandoc_md}")
    return final_pdf.resolve()

# ---------- CLI ----------
def main(argv=None):
    ap=argparse.ArgumentParser(
        description="PNPMD → PDF (Pandoc + crossref; TOC after Keywords; spacing; link/anchor sugar).")
    ap.add_argument("file",nargs="?",help="Markdown file; if omitted, exactly one .md in CWD is required.")
    ap.add_argument("--timeout",type=int,default=0,help="Timeout seconds (0=no timeout).")
    ap.add_argument("--omit-toc",action="store_true",
        help="Do not include a table of contents in the final PDF (disables [[TOC]] insertion and --toc).")
    ap.add_argument("--omit-numbering",action="store_true",
        help="Disable section numbering in the final PDF.")
    ap.add_argument("--as-is",action="store_true",
        help="Bypass preprocessing and pass the original Markdown directly to Pandoc.")
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
