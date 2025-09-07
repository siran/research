#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import os, re, subprocess, shutil
from datetime import datetime, timezone

# ---- config -------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "site"
MAP  = ROOT / "pnpmd.map"
PREPROCESS = ROOT / ".scripts" / "preprocess_pnpmd.py"
MD_GLOBS = ["prints/*/*.md"]         # adjust if you want more locations
BASE_URL = os.getenv("BASE_URL", "").rstrip("/")

# ---- helpers ------------------------------------------------------------
def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def rel(p: Path) -> Path:
    return p.relative_to(ROOT)

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# ---- PNPMD pipeline -----------------------------------------------------
def preprocess_to_pnp(md: Path) -> str:
    """Return preprocessed PNPMD (.pnp.md content)."""
    proc = subprocess.run(
        ["python", str(PREPROCESS), str(md)],
        check=True, capture_output=True, text=True
    )
    # normalize CRLF→LF defensively
    return proc.stdout.replace("\r\n", "\n")

def parse_map_lines(map_text: str):
    """
    Yield (pattern, replacement, is_regex).
    - 'lhs=rhs' literal (lhs is escaped)
    - '/regex/=rhs' regex
    If rhs starts with '\\' (TeX macro), wrap in $...$.
    """
    out = []
    for raw in map_text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"): continue
        if line.startswith("/") and line.count("/") >= 2 and line.rfind("/") > 0:
            # /regex/=rhs
            first = 1
            last = line.rfind("/")
            regex = line[first:last]
            rhs = line[last+2:] if line[last+1: last+2] == "=" else line[last+1:]
            is_regex = True
        else:
            if "=" not in line: continue
            lhs, rhs = line.split("=", 1)
            regex = re.escape(lhs.strip())
            is_regex = True  # treat as regex with escaped lhs
        rhs = rhs.strip()
        if rhs.startswith("\\"):
            rhs = f"${rhs}$"
        out.append((regex, rhs, is_regex))
    return out

def apply_map_to_text(text: str, rules) -> str:
    out = text
    for pat, repl, _ in rules:
        out = re.sub(pat, repl, out)
    return out

def render_pdf(from_md: Path, out_pdf: Path) -> None:
    cmd = [
        "pandoc", str(from_md),
        "--toc", "--toc-depth=2",
        "--number-sections", "--number-offset=1",
        "--reference-links",
        "--citeproc", "-M", "link-citations=true",
        "-F", "pandoc-crossref",
        "--standalone",
        "--shift-heading-level-by=-1",
        "-o", str(out_pdf),
    ]
    # Optional bibliography next to source
    bib = from_md.with_suffix("").with_suffix(".bib")  # uncommon; ignore
    generated_bib = from_md.parent / "generated.bib"
    if generated_bib.exists():
        cmd.extend(["--bibliography", str(generated_bib)])
    run(cmd)

# ---- site generation -----------------------------------------------------
def find_manuscripts() -> list[Path]:
    mds: list[Path] = []
    for g in MD_GLOBS:
        mds.extend(sorted(ROOT.glob(g)))
    # exclude readmes and derived
    mds = [p for p in mds
           if p.name.lower() != "readme.md"
           and not p.name.endswith(".pnp.md")
           and not p.name.endswith(".pnp.pdflatex.md")]
    return mds

def folder_index(md: Path) -> str:
    rel_dir = rel(md.parent).as_posix()
    base = f"{BASE_URL}/{rel_dir}".replace("//","/")
    title = md.stem
    lines = [
        f"## {title}",
        "",
        "Available files:",
        "",
        f"[Markdown]({base}/{md.name})",
        f"[PNPMD (.pnp.md)]({base}/{md.name}.pnp.md)",
        f"[PNPMD (pdflatex) (.pnp.pdflatex.md)]({base}/{md.name}.pnp.pdflatex.md)",
        f"[PDF]({base}/{md.stem}.pdf)",
        "",
        "---",
        '<meta charset="utf-8">',
        "<style>*{white-space:pre-wrap;font-family:monospace}</style>",
    ]
    return "\n".join(lines)

def root_index(mds: list[Path]) -> str:
    lines = [
        "# Research",
        "",
        "---",
        "## Latest documents",
        "",
    ]
    for p in mds:
        rel_dir = rel(p.parent).as_posix()
        url = f"{BASE_URL}/{rel_dir}/".replace("//","/")
        lines.append(f"- [{p.stem}]({url})")
    lines += [
        "",
        f"(updated: {now_iso()})",
        "",
        "---",
        '<meta charset="utf-8">',
        "<style>*{white-space:pre-wrap;font-family:monospace}</style>",
    ]
    return "\n".join(lines)

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    mds = find_manuscripts()
    if not mds:
        write_text(OUT / "index.html", "# Research\n\nNo manuscripts found.\n")
        return

    map_rules = parse_map_lines(MAP.read_text(encoding="utf-8")) if MAP.exists() else []

    staged = []
    for md in mds:
        rel_dir = rel(md.parent)
        # 1) stage originals
        dst_dir = OUT / rel_dir
        dst_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md, dst_dir / md.name)

        # 2) .pnp.md
        pnp_text = preprocess_to_pnp(md)
        pnp_path = dst_dir / (md.name + ".pnp.md")
        write_text(pnp_path, pnp_text)

        # 3) .pnp.pdflatex.md
        pnp_tex_text = apply_map_to_text(pnp_text, map_rules) if map_rules else pnp_text
        pnp_tex_path = dst_dir / (md.name + ".pnp.pdflatex.md")
        write_text(pnp_tex_path, pnp_tex_text)

        # 4) PDF from .pnp.pdflatex.md
        pdf_path = dst_dir / (md.stem + ".pdf")
        render_pdf(pnp_tex_path, pdf_path)

        # 5) per-folder index
        write_text(dst_dir / "index.html", folder_index(md))

        staged.append(md)

    # root index
    write_text(OUT / "index.html", root_index(staged))

if __name__ == "__main__":
    main()
