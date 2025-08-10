# scripts/build_site.py
from pathlib import Path
import html, urllib.parse, datetime

OWNER = "siran"
REPO = "research"
BRANCH = "main"  # adjust if needed
BASE = f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/"

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"

# choose what to list
INCLUDE_EXT = {".pdf", ".md", ".rst", ".txt", ".ipynb"}  # extend if you like
EXCLUDE_TOP = {".git", ".github", "site", "scripts"}

def enc_path(p: Path) -> str:
    return "/".join(urllib.parse.quote(s) for s in p.parts)

def collect():
    files = []
    for p in ROOT.rglob("*"):
        if any(part in EXCLUDE_TOP for part in p.parts[:1]):
            continue
        if p.is_file() and (not INCLUDE_EXT or p.suffix.lower() in INCLUDE_EXT):
            files.append(p.relative_to(ROOT))
    return sorted(files, key=lambda x: str(x).lower())

def build():
    OUT.mkdir(parents=True, exist_ok=True)
    items = []
    for rel in collect():
        href = BASE + enc_path(rel)
        name = html.escape(str(rel))
        items.append(f'<li><a href="{href}">{name}</a></li>')
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    html_doc = f"""<!doctype html>
<meta charset="utf-8">
<title>research — index</title>
<style>
 body{{font:16px/1.55 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}
 h1{{margin:.2rem 0 1rem}} .meta{{opacity:.7;font-size:.9em;margin:.5rem 0 1.5rem}}
 ul{{list-style:none;padding:0}} li{{margin:.25rem 0}} a{{text-decoration:none}} a:hover{{text-decoration:underline}}
</style>
<h1>research</h1>
<p class="meta">Auto-indexed {now}. Links open in GitHub’s viewer.</p>
<ul>
{''.join(items)}
</ul>
<p class="meta">Tip: add <code>?raw=1</code> to a blob URL for direct download.</p>
"""
    (OUT / "index.html").write_text(html_doc, encoding="utf-8")

if __name__ == "__main__":
    build()
