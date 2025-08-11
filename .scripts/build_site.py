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
    """Return (modified_iso, created_iso). Fallback to filesystem if not in git."""
    relp = rel(path).as_posix()
    try:
        m = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%cI", "--", relp],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
        if not m: raise RuntimeError
    except Exception:
        st = path.stat(); m = iso_from_ts(st.st_mtime)
    try:
        c_lines = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--pretty=%cI", "--", relp],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).splitlines()
        c = c_lines[-1] if c_lines else m
    except Exception:
        st = path.stat(); c = iso_from_ts(st.st_ctime)
    return m, c

def render_readme_root() -> str:
    md = ROOT / "README.md"
    if not md.exists(): return ""
    html_body = markdown.markdown(md.read_text(encoding="utf-8"))
    return f'<div class="readme">{html_body}</div>'

def write_page(dir_abs: Path, entries: list[dict], outname: str,
               active_label: str, sort_key):
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

    # order switcher (default page = Modified)
    base = "/research/" + (enc(rel_dir) + "/" if rel_dir.parts else "")
    items = [("index.html","Modified"), ("index_name.html","Name"), ("index_created.html","Created")]
    order_links = " · ".join(
        f"<strong>{lbl}</strong>" if lbl == active_label else f'<a href="{base}{fname}">{lbl}</a>'
        for fname, lbl in items
    )
    switcher = f'<div class="switcher">Order by: {order_links}</div>'

    # sort & render a single mixed list
    mixed = sorted(entries, key=sort_key)
    li = []
    for e in mixed:
        if e["is_dir"]:
            href = f'/research/{enc(rel(e["path"]))}/'
            li.append(
                f'<li><span>📁 </span><a href="{href}">{html.escape(e["name"])}</a> '
                f'<small style="opacity:.7">[mod {e["modified"][:10]} · crt {e["created"][:10]}]</small></li>'
            )
        else:
            raw_url = f"{BASE_BLOB}{enc(rel(e['path']))}?raw=1"
            gh_url  = f"{BASE_BLOB}{enc(rel(e['path']))}"
            li.append(
                f'<li><span>📄 </span><a href="{raw_url}">{html.escape(e["name"])}</a> '
                f'<small style="opacity:.7">[mod {e["modified"][:10]} · crt {e["created"][:10]}]</small> '
                f'<a href="{gh_url}" title="View on GitHub"><img class="gh-icon" '
                f'src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"></a></li>'
            )

    body = [switcher]
    if not rel_dir.parts: body.insert(0, render_readme_root())
    body.append('<ul class="list">' + "".join(li) + "</ul>")
    (out_dir / outname).write_text(head + "\n".join(body) + theme.footer(), encoding="utf-8")

def collect_entries(dir_abs: Path, dirnames: list[str], filenames: list[str]) -> list[dict]:
    entries: list[dict] = []

    # include directories
    for d in dirnames:
        p = dir_abs / d
        mod, crt = git_dates(p)
        entries.append({"name": d + "/", "is_dir": True, "modified": mod, "created": crt, "path": p})

    # include files
    for f in filenames:
        p = dir_abs / f
        if INCLUDE_EXT and p.suffix.lower() not in INCLUDE_EXT: continue
        mod, crt = git_dates(p)
        entries.append({"name": f, "is_dir": False, "modified": mod, "created": crt, "path": p})

    return entries

def build_all_lists(dir_abs: Path, dirnames: list[str], filenames: list[str]):
    entries = collect_entries(dir_abs, dirnames, filenames)

    # name ordering; pin README.md first on root ONLY for Name view
    def name_sorted(es: list[dict]) -> list[dict]:
        es2 = sorted(es, key=lambda e: e["name"].lower())
        if rel(dir_abs).parts: return es2
        # bubble README.md (file) to top on root
        es2.sort(key=lambda e: (not (not e["is_dir"] and e["name"].lower() == "readme.md"), e["name"].lower()))
        return es2

    orders = [
        ("index.html",         "Modified", lambda e: (e["modified"], e["name"].lower())),  # DEFAULT
        ("index_name.html",    "Name",     lambda e: e["name"].lower()),
        ("index_created.html", "Created",  lambda e: (e["created"],  e["name"].lower())),
    ]
    for outname, label, key in orders:
        entries_for_view = name_sorted(entries) if label == "Name" else entries
        write_page(dir_abs, entries_for_view, outname, label, key)

def main():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if dirpath != str(ROOT) and Path(dirpath).relative_to(ROOT).parts[0] in EXCLUDE_TOP:
            dirnames.clear(); continue
        # prune hidden dirs/files (except .well-known)
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_TOP and not (d.startswith(".") and d != ".well-known")]
        filenames = [f for f in filenames if not f.startswith(".")]
        build_all_lists(Path(dirpath), dirnames, filenames)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    main()
