#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
renderpdf.py — PNPMD renderer (Python)
- Can be imported:  from renderpdf import renderpdf; renderpdf("file.md")
- Can be executed:  python renderpdf.py file.md
- If no file is given: requires exactly one .md in CWD (non-hidden, not name.*.md)
- Pipeline: read pnpmd.map → apply sequential mappings → write .pnp.md → run pandoc
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ------------------------- helpers -------------------------

def repo_root_or_cwd() -> Path:
    """Return git toplevel if inside a repo; else CWD."""
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL)
        p = Path(out.decode().strip())
        if p.exists():
            return p
    except Exception:
        pass
    return Path.cwd()

def discover_md_in_cwd() -> Path:
    """
    Return the unique .md in CWD if exactly one exists (non-hidden, not name.*.md).
    Raise RuntimeError otherwise.
    """
    cwd = Path.cwd()
    cands = [p for p in cwd.iterdir()
             if p.is_file()
             and p.suffix.lower() == ".md"
             and not p.name.startswith(".")
             and not re.search(r"\.[A-Za-z0-9_-]+\.md$", p.name)]
    if len(cands) == 1:
        return cands[0]
    if len(cands) == 0:
        raise RuntimeError("No .md in current directory.")
    names = "\n".join(f" - {p.name}" for p in sorted(cands))
    raise RuntimeError(f"Ambiguous: multiple .md files in CWD:\n{names}\nSpecify the file explicitly.")

def load_map_lines(map_path: Path):
    """Yield (lhs, rhs, is_regex) for each non-comment, non-empty line in pnpmd.map."""
    if not map_path.exists():
        return []
    entries = []
    with map_path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip("\n")
            if not line or line.lstrip().startswith("#"):
                continue
            if "=" not in line:
                continue
            lhs, rhs = line.split("=", 1)
            lhs = lhs.strip()
            rhs = rhs.strip()
            # regex rule if lhs is /.../ with single leading+trailing slash
            is_regex = (len(lhs) >= 2 and lhs.startswith("/") and lhs.endswith("/"))
            entries.append((lhs, rhs, is_regex))
    return entries

def apply_mappings(text: str, entries) -> str:
    """
    Apply mappings sequentially.
    - If RHS starts with "\" (TeX macro), auto-wrap as $RHS$.
    - Regex rule: lhs like /.../
    - Literal rule: re.escape(lhs)
    - Replacement is literal (no backref expansion).
    """
    for lhs, rhs, is_regex in entries:
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs

        # Use a lambda to prevent backref escapes in the replacement
        if is_regex:
            pattern = lhs[1:-1]
            try:
                regex = re.compile(pattern)
            except re.error as e:
                raise RuntimeError(f"Invalid regex in map: {lhs} ({e})")
            text = regex.sub(lambda m, _rep=rep: _rep, text)
        else:
            pattern = re.escape(lhs)
            text = re.sub(pattern, lambda m, _rep=rep: _rep, text)
    return text

def normalize_crlf(s: str) -> str:
    """Convert CRLF to LF (leave lone CR alone if ever present)."""
    return s.replace("\r\n", "\n")

def which(cmd: str) -> str | None:
    return shutil.which(cmd)

def docker_has_pandoc_crossref() -> bool:
    try:
        subprocess.run(
            ["docker", "run", "--rm", "-i", "pandoc/latex", "pandoc-crossref", "-v"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
        return True
    except Exception:
        return False

def local_has(cmd: str) -> bool:
    return which(cmd) is not None

def run_pandoc(root: Path, pnp_rel: Path, out_rel: Path) -> None:
    """
    Try dockerized pandoc/latex first; fall back to local pandoc.
    Include crossref filter if available.
    """
    # Common args
    base_args = [
        "--toc", "--toc-depth=2", "--number-sections", "--reference-links",
        "--citeproc", "-M", "link-citations=true", "--standalone"
    ]

    # 1) Docker path
    docker_ok = local_has("docker")
    xref_flag = []
    if docker_ok and docker_has_pandoc_crossref():
        xref_flag = ["-F", "pandoc-crossref"]

    if docker_ok:
        cmd = [
            "docker", "run", "--rm", "-i",
            "-v", f"{str(root)}:/data", "-w", "/data",
            "pandoc/latex",
            *base_args, *xref_flag,
            str(pnp_rel), "-o", str(out_rel)
        ]
        r = subprocess.run(cmd)
        if r.returncode == 0:
            return
        # if docker failed, try local

    # 2) Local pandoc
    xref_local = ["-F", "pandoc-crossref"] if local_has("pandoc-crossref") else []
    if not local_has("pandoc"):
        raise RuntimeError("pandoc not found (docker failed/unavailable, and no local pandoc).")
    cmd = ["pandoc", *base_args, *xref_local, str(root / pnp_rel), "-o", str(root / out_rel)]
    r = subprocess.run(cmd)
    if r.returncode != 0:
        raise RuntimeError("Pandoc build failed.")

# ------------------------- main op -------------------------

def renderpdf(file_md: str | os.PathLike | None = None) -> Path:
    """
    Process PNPMD:
    - select input .md (explicit or unique in CWD)
    - apply pnpmd.map (repo root)
    - write .pnp.md next to input (relative to root)
    - render to PDF via pandoc (docker or local)
    Returns: Path to the produced PDF (absolute).
    """
    root = repo_root_or_cwd()
    map_path = root / "pnpmd.map"

    # choose input
    if file_md is None:
        src = discover_md_in_cwd()
    else:
        src = Path(file_md)
        if not src.exists():
            raise FileNotFoundError(str(src))

    # compute relative paths (container I/O uses /data mount)
    rel = Path(os.path.relpath(src, root))
    out_rel = rel.with_suffix(".pdf")
    pnp_rel = rel.with_suffix(".pnp.md")

    # read + preprocess
    text = src.read_text(encoding="utf-8")
    text = normalize_crlf(text)
    entries = load_map_lines(map_path)
    if entries:
        print(f"Using map: {map_path}")
    processed = apply_mappings(text, entries) if entries else text

    # ensure directory for interim
    (root / pnp_rel).parent.mkdir(parents=True, exist_ok=True)
    (root / pnp_rel).write_text(processed, encoding="utf-8")

    # render
    run_pandoc(root, pnp_rel, out_rel)

    print(f"✅ Wrote {out_rel}  (source: {pnp_rel})")
    return (root / out_rel).resolve()

# ------------------------- CLI -------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="renderpdf.py",
        description="PNPMD renderer: map → .pnp.md → PDF via pandoc."
    )
    ap.add_argument("file", nargs="?", help="Markdown file. If omitted, requires exactly one .md in CWD.")
    args = ap.parse_args(argv)
    try:
        renderpdf(args.file)
    except Exception as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
