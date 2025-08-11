import os, html, urllib.parse, datetime, subprocess
from pathlib import Path
from zoneinfo import ZoneInfo
import markdown  # pip install markdown
import theme

# CONFIG
OWNER, REPO, BRANCH = "siran", "research", "main"
INCLUDE_EXT = set()            # empty = include all
EXCLUDE_TOP = {"site"}
NYC = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
BASE_BLOB = f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/"

def enc(p: Path) -> str: return "/".join(urllib.parse.quote(x) for x in p.parts)
def rel(p: Path) -> Path: return p.relative_to(ROOT)

def iso_from_ts(ts: float) -> str:
    return datetime.datetime.fromtimestamp(ts, NYC).astimezone(ZoneInfo("UTC")).isoformat()

def git_dates(path: Path) -> tuple[str, str]:
    """Return (modified_iso, created_iso). Fallback to filesystem times if git unavailable."""
    relp = rel(path).as_posix()
    try:
        m = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%cI", "--", relp],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
        if not m:  # untracked
            raise RuntimeError
    except Exception:
        st = path.stat()
        m = iso_from_ts(st.st_mtime)
    try:
        c = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--pretty=%cI", "--", relp],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).splitlines()
        c = c[-1] if c else m
    except Exception:
        st = path.stat()
        c = iso_from_ts(st.st_ctime)
    return m, c

def render_readme_root() -> str:
    md = ROOT / "README.md"
    if not md.exists(): return ""
    html_body = markdown.markdown(md.read_text(encoding="utf-8"))
    return f'<div class="readme">{html_body}</div>'

def write_page(dir_abs: Path, dirs: list[str], entries: list[dict],
               outname: str, active_label: str, sort_key):
    rel_dir = rel(dir_abs)
    out_dir = OUT / rel_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # breadcrumbs
    crumbs = ['<span class="crumbs"><a href="/research/">Home</a>']
    sofar = Path()
    for part in rel_dir.parts:
        sofar /= part
        crumbs.append(f' / <a href="/research/{enc(sofar)}/">{html.escape(part)}</a>')
    crumbs.append("</span>")

    now = datetime.datetime.now(NYC).strftime("%Y-%m-%d %H:%M %Z")
    subtitle = f'Indexed {now}. {theme.SITE_NOTE}<br>{"".join(crumbs)}'

    # <title> tag and H1
    label = "/".join(rel_dir.parts) or "Home"
    page_title = f"{theme.SITE_TITLE} — {label}" if rel_dir.parts else theme.SITE_TITLE
    display_h1 = f'<a href="/research/">{html.escape(label)}</a>' if rel_dir.parts else html.escape(theme.SITE_TITLE)
    head = theme.header(display_h1, subtitle, page_title)

    # order switcher
    base = "/research/" + (enc(rel_dir) + "/" if rel_dir.parts else "")
    items = [("index.html", "Name"), ("index_mod.html", "Modified"), ("index_created.html", "Created")]
    order_links = " · ".join(
        f"<strong>{lbl}</strong>" if lbl == active_label else f'<a href="{base}{fname}">{lbl}</a>'
        for fname, lbl in items
    )
    switcher = f'<div class="switcher">Order by: {order_links}</div>'

    # directories
    li_dirs = [
        f'<li><a href="/research/{enc(rel(dir_abs/d))}/">{html.escape(d)}/</a></li>'
        for d in sorted(dirs)
    ]

    # files (sorted)
    files_sorted = sorted(entries, key=sort_key)
    li_files = []
    for e in files_sorted:
        raw_url = f"{BASE_BLOB}{enc(rel(e['path']))}?raw=1"
        gh_url  = f"{BASE_BLOB}{enc(rel(e['path']))}"
        li_files.append(
            f'<li><a href="{raw_url}">{html.escape(e["name"])}</a> '
            f'<small style="opacity:.7">[mod {e["modified"][:10]} · crt {e["created"][:10]}]</small> '
            f'<a href="{gh_url}" title="View on GitHub"><img class="gh-icon" '
            f'src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"></a></li>'
        )

    # assemble
    body = [switcher]
    if not rel_dir.parts: body.insert(0, render_readme_root())
    if li_dirs:  body.append('<ul class="dirs">'  + "".join(li_dirs)  + "</ul>")
    if li_files: body.append('<ul class="files">' + "".join(li_files) + "</ul>")
    (out_dir / outname).write_text(head + "\n".join(body) + theme.footer(), encoding="utf-8")

def build_all_lists(dir_abs: Path, dirs: list[str], files: list[str]):
    # gather entries with git dates
    entries = []
    for f in files:
        p = dir_abs / f
        if INCLUDE_EXT and p.suffix.lower() not in INCLUDE_EXT: continue
        modified, created = git_dates(p)
        entries.append({"name": f, "modified": modified, "created": created, "path": p})

    # pin README.md on root (for all orderings)
    def pin_readme(seq):
        if rel(dir_abs).parts: return sorted(seq, key=lambda e: e["name"].lower())
        return sorted(seq, key=lambda e: (e["name"].lower() != "readme.md", e["name"].lower()))

    orders = [
        ("index.html",        "Name",     lambda e: e["name"].lower()),
        ("index_mod.html",    "Modified", lambda e: (e["modified"], e["name"].lower())),
        ("index_created.html","Created",  lambda e: (e["created"],  e["name"].lower())),
    ]
    for outname, label, key in orders:
        write_page(dir_abs, dirs, pin_readme(entries), outname, label, key)

def main():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if dirpath != str(ROOT) and Path(dirpath).relative_to(ROOT).parts[0] in EXCLUDE_TOP:
            dirnames.clear(); continue
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_TOP and not (d.startswith(".") and d != ".well-known")]
        filenames = [f for f in filenames if not f.startswith(".")]
        build_all_lists(Path(dirpath), dirnames, filenames)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    main()
