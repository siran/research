#!/usr/bin/env python3
"""
renderpdf.py

Usage:
  python renderpdf.py [--verbose] [--as-is] <docname>.md

Default pipeline:
  1) Read <docname>.md
  2) Convert standalone {#id} -> []{#id} (no code, no ATX headers, **no colons**)
  3) Replace bare @id -> [id](#id) iff []{#id} exists (never touch any @...:...)
  4) Write <docname>.pnp.md
  5) Run Pandoc (pandoc/extra) with pandoc-crossref -> <docname>.pdf

With --as-is:
  - Skip steps 2–4; use original .md
"""

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Dict

# Regexes
ANCHOR_BRACE_RE = re.compile(r"\{#([A-Za-z0-9:_-]+)\}")            # {#id}
ANCHOR_EMPTY_SPAN_RE = re.compile(r"\[\]\{#([A-Za-z0-9:_-]+)\}")    # []{#id}
AT_TOKEN_RE = re.compile(r"(?<!\w)@([A-Za-z0-9:_-]+)")              # bare @id

# Fenced code blocks: ```...``` or ~~~...~~~
FENCE_RE = re.compile(r"(?ms)^(?:```+|~~~+)[^\n]*\n.*?^(?:```+|~~~+)\s*$")

# Inline code spans: `...`
INLINE_CODE_RE = re.compile(r"(?s)`[^`]*`")

# ATX headers: optional indent (0–3), then 1–6 #'s
ATX_HEADER_LINE_RE = re.compile(r"^[ \t]{0,3}#{1,6}\b")

def _excluded_ranges(text: str) -> List[Tuple[int,int]]:
    ranges: List[Tuple[int,int]] = []
    for m in FENCE_RE.finditer(text):
        ranges.append((m.start(), m.end()))
    for m in INLINE_CODE_RE.finditer(text):
        ranges.append((m.start(), m.end()))
    ranges.sort()
    merged: List[Tuple[int,int]] = []
    for s,e in ranges:
        if not merged or s > merged[-1][1]:
            merged.append((s,e))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    return merged

def _in_ranges(pos: int, ranges: List[Tuple[int,int]]) -> bool:
    for s,e in ranges:
        if s <= pos < e: return True
        if pos < s: return False
    return False

def _line_starts(text: str) -> List[int]:
    ls = [0]
    for m in re.finditer(r"\n", text):
        ls.append(m.end())
    return ls

def _linecol(pos: int, line_starts: List[int]) -> Tuple[int,int]:
    lo, hi = 0, len(line_starts)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if line_starts[mid] <= pos:
            lo = mid+1
        else:
            hi = mid-1
    line = hi + 1
    col = pos - line_starts[hi] + 1
    return line, col

def convert_brace_to_empty_spans(text: str) -> Tuple[str, int, List[Dict]]:
    """
    Convert standalone {#id} -> []{#id} when:
      - not in code
      - not on ATX header lines
      - not already []{#id}
      - **id has NO colon**
    Returns (new_text, count, changes)
    """
    ex = _excluded_ranges(text)
    ls = _line_starts(text)
    out = []
    i = 0
    changes: List[Dict] = []
    count = 0

    for m in ANCHOR_BRACE_RE.finditer(text):
        s, e = m.span()
        idname = m.group(1)
        out.append(text[i:s])

        if _in_ranges(s, ex):
            out.append(text[s:e]); i = e; continue

        # On a header line? leave as-is
        linestart = text.rfind("\n", 0, s) + 1
        line = text[linestart : text.find("\n", linestart) if text.find("\n", linestart) != -1 else len(text)]
        if ATX_HEADER_LINE_RE.match(line):
            out.append(text[s:e]); i = e; continue

        # Already []{#id} (immediately preceded by "[]")?
        if s >= 2 and text[s-2:s] == "[]":
            out.append(text[s:e]); i = e; continue

        # NEW: skip ids with colon (e.g., eq:..., fig:..., etc.)
        if ":" in idname:
            out.append(text[s:e]); i = e; continue

        repl = f"[]{{#{idname}}}"
        out.append(repl)
        ln, col = _linecol(s, ls)
        changes.append({"type":"anchor", "line": ln, "col": col,
                        "token": f"{{#{idname}}}", "replacement": repl})
        count += 1
        i = e

    out.append(text[i:])
    return "".join(out), count, changes

def replace_at_with_links(text: str) -> Tuple[str, int, List[Dict]]:
    """
    Replace @id -> [id](#id) iff []{#id} exists (post-conversion).
    Never change tokens that contain a colon (i.e., @...:...).
    Skip code, and avoid double-linking (already followed by ](#id)).
    Returns (new_text, num_replaced, changes)
    """
    # Only consider ids present as EMPTY SPANS
    span_ids = set(ANCHOR_EMPTY_SPAN_RE.findall(text))

    ex = _excluded_ranges(text)
    ls = _line_starts(text)
    out = []
    i = 0
    replaced = 0
    changes: List[Dict] = []

    for m in AT_TOKEN_RE.finditer(text):
        s, e = m.span()
        name = m.group(1)
        out.append(text[i:s])

        if _in_ranges(s, ex):
            out.append(text[s:e]); i = e; continue

        # Skip crossref-like tokens (contain colon)
        if ":" in name:
            out.append(text[s:e]); i = e; continue

        # Only link if empty-span anchor exists
        if name not in span_ids:
            out.append(text[s:e]); i = e; continue

        # Avoid double-linking
        if text[e : e + len(f"](#{name})")] == f"](#{name})":
            out.append(text[s:e]); i = e; continue

        repl = f"[{name}](#{name})"
        out.append(repl)
        ln, col = _linecol(s, ls)
        changes.append({"type":"link", "line": ln, "col": col,
                        "token": f"@{name}", "replacement": repl})
        replaced += 1
        i = e

    out.append(text[i:])
    return "".join(out), replaced, changes

def run_pandoc_in_docker(md_in: Path, pdf_out: Path, verbose: bool) -> int:
    cmd = [
        "docker", "run", "--rm",
        "--mount", f"type=bind,source={md_in.parent.resolve()},target=/data",
        "-w", "/data",
        "pandoc/extra",
        "--standalone",
        "--number-sections",
        "--toc", "--toc-depth=2",
        "--filter", "pandoc-crossref",
        "-f", "markdown",
        md_in.name,
        "-o", pdf_out.name,
    ]
    print("[cmd]", " ".join(cmd))
    return subprocess.run(cmd, check=True).returncode

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true", help="Print extra info")
    ap.add_argument("--as-is", action="store_true", help="Skip preprocessing; use original .md")
    ap.add_argument("mdfile", help="Input Markdown file, e.g., doc.md")
    args = ap.parse_args()

    in_path = Path(args.mdfile)
    if not in_path.exists() or in_path.suffix.lower() != ".md":
        print("Error: provide an existing .md file", file=sys.stderr)
        sys.exit(1)

    docname = in_path.stem
    pnp_md = in_path.with_name(f"{docname}.pnp.md")
    pdf_out = in_path.with_suffix(".pdf")

    if args.as_is:
        print("[info] --as-is: preprocessing skipped; using original .md")
        try:
            rc = run_pandoc_in_docker(in_path, pdf_out, args.verbose)
            if rc == 0:
                print(f"OK: wrote {pdf_out.name} (from {in_path.name})")
            sys.exit(rc)
        except subprocess.CalledProcessError as e:
            print(f"[pandoc] failed with exit code {e.returncode}", file=sys.stderr)
            sys.exit(e.returncode)

    # Preprocess
    src = in_path.read_text(encoding="utf-8")

    # Step 1: {#id} -> []{#id} (standalone only, no colons)
    converted, n_anchor_conv, anchor_changes = convert_brace_to_empty_spans(src)

    # Step 2: @id -> [id](#id) only if []{#id} exists
    transformed, n_links, link_changes = replace_at_with_links(converted)

    # Write .pnp.md
    pnp_md.write_text(transformed, encoding="utf-8")

    # Logs
    span_anchor_count = len(set(ANCHOR_EMPTY_SPAN_RE.findall(transformed)))
    print(f"[info] empty-span anchors detected ([]{{#...}}): {span_anchor_count}")
    if args.verbose and span_anchor_count:
        sample = sorted(set(ANCHOR_EMPTY_SPAN_RE.findall(transformed)))[:12]
        print(f"[info] sample anchors: {sample}")
    print(f"[info] brace-anchors converted: {n_anchor_conv}")
    print(f"[info] @id -> links made: {n_links}")

    # Detailed changes
    if anchor_changes or link_changes:
        print("[changes]")
        for c in anchor_changes + link_changes:
            print(f"  line {c['line']}, col {c['col']}: {c['token']} -> {c['replacement']}")

    # Unified diff
    print("[diff] unified diff (.md -> .pnp.md):")
    diff = difflib.unified_diff(
        src.splitlines(keepends=False),
        transformed.splitlines(keepends=False),
        fromfile=in_path.name,
        tofile=pnp_md.name,
        lineterm=""
    )
    for line in diff:
        print(line)

    # Pandoc
    try:
        rc = run_pandoc_in_docker(pnp_md, pdf_out, args.verbose)
        if rc == 0:
            print(f"OK: wrote {pdf_out.name} (from {pnp_md.name})")
        sys.exit(rc)
    except subprocess.CalledProcessError as e:
        print(f"[pandoc] failed with exit code {e.returncode}", file=sys.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
