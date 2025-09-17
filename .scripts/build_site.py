#!/usr/bin/env python3
import os, html, datetime, urllib.parse
from pathlib import Path
from dataclasses import dataclass

# ---- config ----
OWNER, REPO, BRANCH = "siran", "research", "main"
ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "site"
EXCLUDE_TOP = {"site","venv",".venv","env",".env","node_modules",".git","__pycache__",
               ".mypy_cache",".pytest_cache",".ruff_cache",".cache"}
BASE_PATH = os.getenv("SITE_BASE", f"/{REPO}/")  # e.g. "/research/" on Pages; "/" locally


def rel(p: Path) -> Path: return p.relative_to(ROOT)
def raw_url(path_from_root: Path) -> str:
    return f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{urllib.parse.quote(path_from_root.as_posix())}"
def blob_url(path_from_root: Path) -> str:
    return f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/{urllib.parse.quote(path_from_root.as_posix())}"

def prune_dirs(root: str, dirnames: list[str]):
    keep=[]
    for d in dirnames:
        if d in EXCLUDE_TOP: continue
        if d.startswith(".") and d != ".well-known": continue
        if (Path(root)/d/"pyvenv.cfg").exists(): continue
        keep.append(d)
    dirnames[:] = keep

@dataclass
class Item:
    name: str
    is_dir: bool
    mtime: float
    path: Path

INDEX_STYLE = """<style>
html,body{background:#fff;color:#111;margin:0;font:16px/1.55 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
main{max-width:960px;margin:2rem auto;padding:0 1rem}
h1{margin:.2rem 0 0;font-weight:650}
.sub{color:#666;font-size:.95rem;margin:.25rem 0 1rem}
.list{list-style:none;margin:0;padding:0}
.row{display:flex;align-items:center;gap:.75rem;padding:.55rem .6rem;border:1px solid #e5e7eb;border-radius:.55rem;margin:.4rem 0}
.row:hover{background:#f8fafc}
.icon{width:1.25rem;text-align:center}
.name{flex:1;min-width:240px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.meta{display:flex;gap:1rem;color:#666;font-size:.92rem}
.badges{display:flex;gap:.35rem;flex-wrap:wrap}
.badge{font-size:.86rem;border:1px solid #e5e7eb;background:#fff;color:inherit;border-radius:.5rem;padding:.15rem .4rem;text-decoration:none}
.crumbs a{color:inherit;text-decoration:none}
footer{margin:3rem 0 2rem;color:#666;font-size:.9rem}
</style>"""

def fmt_local(ts: float) -> str:
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")

def write_index(dir_abs: Path, items: list[Item]):
    rel_dir = rel(dir_abs) if dir_abs != ROOT else Path()
    out_dir = OUT / rel_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # Home should always point to site root (/research/)
    crumbs = [f'<span class="crumbs"><a href="{BASE_PATH}">Home</a>']
    parts = list(rel_dir.parts)
    for i,p in enumerate(parts):
        up = "../"*(len(parts)-i-1) or "./"
        crumbs.append(f' / <a href="{up}">{html.escape(p)}</a>')
    crumbs.append("</span>")

    title = (rel_dir.name or "SIRAN's Research")
    subtitle = f'{ "".join(crumbs) }'

    # folders first, then files (both A→Z)
    items_sorted = sorted(items, key=lambda e: (not e.is_dir, e.name.lower()))

    rows=[]
    for it in items_sorted:
        icon = "📁" if it.is_dir else "📄"
        if it.is_dir:
            href = (rel(it.path).name + "/") if rel_dir.parts else (rel(it.path).as_posix() + "/")
            link = f'<a href="{href}">{html.escape(it.name)}</a>'
            meta = f'<span>dir</span>'
        else:
            p_rel = rel(it.path)
            link = (f'{html.escape(it.name)} '
                    f'<span class="badges">'
                    f'<a class="badge" href="{blob_url(p_rel)}">github</a> '
                    f'<a class="badge" href="{raw_url(p_rel)}">raw</a>'
                    f'</span>')
            meta = f'<span>file</span><span>modified {html.escape(fmt_local(it.mtime))}</span>'
        rows.append(
            f'<li class="row">'
            f'<span class="icon">{icon}</span>'
            f'<div class="name">{link}</div>'
            f'<div class="meta">{meta}</div>'
            f'</li>'
        )

    html_doc = f"""<!doctype html>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="data:,">
{INDEX_STYLE}
<main>
  <h1>{html.escape(title)}</h1>
  <div class="sub">{subtitle}</div>
  <ul class="list">
{''.join(rows)}
  </ul>
  <footer>© {datetime.datetime.now().year} SIRAN • Built from {OWNER}/{REPO}@{BRANCH}</footer>
</main>
"""
    (out_dir/"index.html").write_text(html_doc, encoding="utf-8")

def main():
    OUT.mkdir(exist_ok=True)
    (OUT/".nojekyll").write_text("", encoding="utf-8")

    # create index per directory (no git calls, no copies)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if Path(dirpath) == OUT:
            dirnames.clear(); continue
        if dirpath != str(ROOT):
            first = Path(dirpath).relative_to(ROOT).parts[0]
            if first in EXCLUDE_TOP:
                dirnames.clear(); continue
            if (Path(dirpath)/"pyvenv.cfg").exists():
                dirnames.clear(); continue
        prune_dirs(dirpath, dirnames)

        d = Path(dirpath)
        items: list[Item] = []

        for name in sorted([x.name for x in d.iterdir() if x.is_dir()], key=str.lower):
            p = d / name
            if name in EXCLUDE_TOP: continue
            if name.startswith(".") and name != ".well-known": continue
            if (p/"pyvenv.cfg").exists(): continue
            mtime = p.stat().st_mtime
            items.append(Item(name=name, is_dir=True, mtime=mtime, path=p))

        for name in sorted([x.name for x in d.iterdir() if x.is_file() and not x.name.startswith(".")], key=str.lower):
            p = d / name
            mtime = p.stat().st_mtime
            items.append(Item(name=name, is_dir=False, mtime=mtime, path=p))

        write_index(d, items)

if __name__ == "__main__":
    main()
