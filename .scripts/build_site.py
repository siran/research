import os, html, urllib.parse, datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import theme

# CONFIG
OWNER, REPO, BRANCH = "siran", "research", "main"
INCLUDE_EXT = set()  # empty = include all
EXCLUDE_TOP = {"site"}
NYC = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
BASE_BLOB = f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/"

def enc(p: Path) -> str:
    return "/".join(urllib.parse.quote(x) for x in p.parts)

def rel(p: Path) -> Path:
    return p.relative_to(ROOT)

def build_index(dir_abs: Path, dirs: list[str], files: list[str]):
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
    subtitle = f'{theme.SITE_NOTE} &nbsp;|&nbsp; Indexed {now}.<br>{"".join(crumbs)}'
    head = theme.header(f"{theme.SITE_TITLE} — {str(rel_dir) or 'root'}", subtitle)

    # directories list (Pages subindexes)
    li_dirs = [
        f'<li><a href="/research/{enc(rel(dir_abs/d))}/">{html.escape(d)}/</a></li>'
        for d in sorted(dirs)
    ]

    # files list: name → raw file, GitHub icon → blob viewer
    def file_items():
        names = sorted(files)
        if not rel_dir.parts:
            # Pin README.md on root
            names.sort(key=lambda n: (n.lower() != "readme.md", n.lower()))
        for f in names:
            if INCLUDE_EXT and Path(f).suffix.lower() not in INCLUDE_EXT:
                continue
            raw_url = f"{BASE_BLOB}{enc(rel(dir_abs/f))}?raw=1"
            gh_url = f"{BASE_BLOB}{enc(rel(dir_abs/f))}"
            yield (
                f'<li><a href="{raw_url}">{html.escape(f)}</a> '
                f'<a href="{gh_url}" title="View on GitHub">'
                f'<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" '
                f'style="height:1em;vertical-align:middle;border:none" alt="GitHub"></a></li>'
            )

    li_files = list(file_items())

    body = []
    if li_dirs:
        body.append('<ul class="dirs">' + "".join(li_dirs) + "</ul>")
    if li_files:
        body.append('<ul class="files">' + "".join(li_files) + "</ul>")

    (out_dir / "index.html").write_text(head + "\n".join(body) + theme.footer(), encoding="utf-8")

def main():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if dirpath != str(ROOT) and Path(dirpath).relative_to(ROOT).parts[0] in EXCLUDE_TOP:
            dirnames.clear()
            continue
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_TOP and not (d.startswith(".") and d != ".well-known")
        ]
        filenames = [f for f in filenames if not f.startswith(".")]
        build_index(Path(dirpath), dirnames, filenames)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    main()
