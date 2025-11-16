#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, urllib.parse, shutil
from pathlib import Path
from dataclasses import dataclass
from urllib.parse import urlparse
from datetime import datetime, date, timezone
from zoneinfo import ZoneInfo

import yaml
from feedgen.feed import FeedGenerator

# ---------- config ----------
EXCLUDE_NAMES = {
    "site","venv",".venv","env",".env","node_modules",".git",
    "__pycache__", ".mypy_cache",".pytest_cache",".ruff_cache",".cache",
    "Makefile","index.html","_staging", "pnpmd.map", "requirements.txt",
    "gpt5push.sh",
}

# ---------- repo autodetect ----------
def _parse_remote(url: str):
    try:
        if url.startswith("git@"):
            path = url.split(":", 1)[1]
        else:
            path = urllib.parse.urlparse(url).path.lstrip("/")
        if path.endswith(".git"): path = path[:-4]
        owner, repo = path.split("/", 1)
        return owner, repo
    except Exception:
        return None, None

def detect_repo_branch():
    owner = os.getenv("SITE_OWNER")
    repo  = os.getenv("SITE_REPO")
    branch= os.getenv("SITE_BRANCH")

    gh = os.getenv("GITHUB_REPOSITORY")  # "owner/repo"
    if gh and "/" in gh:
        o, r = gh.split("/", 1)
        owner = owner or o
        repo  = repo  or r
    branch = branch or os.getenv("GITHUB_REF_NAME")

    if not (owner and repo):
        try:
            url = subprocess.check_output(
                ["git","config","--get","remote.origin.url"],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
            o, r = _parse_remote(url)
            owner = owner or o
            repo  = repo  or r
        except Exception:
            pass
    if not branch:
        try:
            branch = subprocess.check_output(
                ["git","rev-parse","--abbrev-ref","HEAD"],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            branch = "main"

    if not owner: owner = "siran"
    if not repo:  repo  = Path.cwd().name
    return owner, repo, branch

OWNER, REPO, BRANCH = detect_repo_branch()

# ---------- paths ----------
ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "site"
SRC  = ROOT / ".scripts" / "src"  # header.html / footer.html / coda.html

# ---------- base url & CNAME ----------
def compute_base_url() -> str:
    v = os.getenv("BASE_URL")
    if v: return v.rstrip("/")
    if os.getenv("GITHUB_ACTIONS","").lower() == "true":
        return f"https://{OWNER}.github.io/{REPO}"
    return "http://127.0.0.1:8000"

BASE_URL = compute_base_url()

def write_cname_if_custom(base_url: str):
    host = urlparse(base_url).hostname  # strip port
    if not host: return
    if host.endswith(".github.io"): return
    if host in {"localhost", "127.0.0.1"}: return
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "CNAME").write_text(host + "\n", encoding="utf-8")

# ---------- helpers ----------
def rel(p: Path) -> Path: return p.relative_to(ROOT)
def rel_out(p: Path) -> Path: return p.relative_to(OUT)

# keep spaces visible (no encoding)
def raw_url(relpath: Path) -> str:
    return f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{relpath.as_posix()}"

def blob_url(relpath: Path) -> str:
    return f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/{relpath.as_posix()}"

def prune_dirs(root: str, dirnames: list[str]):
    keep=[]
    for d in dirnames:
        if d in EXCLUDE_NAMES: continue
        if d.startswith(".") and d != ".well-known": continue
        if (Path(root)/d/"pyvenv.cfg").exists(): continue
        keep.append(d)
    dirnames[:] = keep

def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

@dataclass
class Item:
    name: str
    is_dir: bool
    mtime: float
    path: Path

# ---------- provenance helpers (for origin + RSS) ----------
def _canonical_origin_from_provenance() -> str | None:
    """
    Infer canonical origin from provenance (top-level 'permalink'
    or site.permalink/html_canonical if present).
    """
    try:
        prints_dir = ROOT / "prints"
        if not prints_dir.exists():
            return None
        for prov in prints_dir.glob("*/*/*/provenance.yaml"):
            try:
                data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
                # new schema
                u = (data.get("permalink") or "").strip()
                # old schema fallbacks
                if not u:
                    site_block = (data.get("site") or {})
                    u = (site_block.get("permalink") or site_block.get("html_canonical") or "").strip()
                if u.startswith("http"):
                    p = urlparse(u)
                    if p.scheme and p.netloc:
                        return f"{p.scheme}://{p.netloc}"
            except Exception:
                continue
    except Exception:
        pass
    return None

def _to_datetime(obj) -> datetime | None:
    if isinstance(obj, datetime): return obj
    if isinstance(obj, date):    return datetime.combine(obj, datetime.min.time())
    if isinstance(obj, str):
        s = obj.strip()
        for fmt in ("%Y-%m-%d","%Y-%m","%Y"):
            try: return datetime.strptime(s, fmt)
            except Exception: pass
    return None

def normalize_authors(auth_list):
    out = []
    for a in (auth_list or []):
        if isinstance(a, dict):
            nm = (a.get("name") or a.get("full_name") or "").strip()
            em = (a.get("email") or "").strip()
        else:
            nm = str(a).strip(); em = ""
        if not nm or nm.lower() == "name":
            continue
        item = {"name": nm}
        if em: item["email"] = em
        out.append(item)
    return out

# ---------- templating ----------
def write_html(out_html: Path, body_html: str, head_extra: str = "", title: str = ""):
    header = load_text(SRC / "header.html")
    footer = load_text(SRC / "footer.html")
    coda   = load_text(SRC / "coda.html")

    # header + body + footer as authored (markdown-ish)
    doc = "".join(s for s in (header, body_html, footer) if s)

    # Timestamp (NY time)
    ny = ZoneInfo("America/New_York")
    now = datetime.now(ny)
    offset = now.utcoffset()
    hrs = int(offset.total_seconds() // 3600) if offset else 0
    stamp = f"(generated at: {now.strftime('%Y-%m-%d %H:%M %Z')} {hrs:+d})"

    if not doc.endswith("\n"):
        doc += "\n"
    doc += stamp

    # Append coda exactly as authored
    if coda:
        doc += coda

    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(doc, encoding="utf-8")

def write_md_like_page(out_html: Path, md_body: str):
    """
    Treat md_body as markdown-like text (index), wrapped with header/footer/coda.
    """
    # no escaping; links are handled by the coda script
    write_html(out_html, md_body)

# ---------- content (pure Markdown body) ----------
def breadcrumbs(rel_dir: Path) -> str:
    depth = len(rel_dir.parts)
    to_root = "./" if depth == 0 else "../" * depth
    crumbs = [f"[🏠 Home]({to_root})"]
    for i, part in enumerate(rel_dir.parts):
        up = "../" * (len(rel_dir.parts) - i - 1) or "./"
        crumbs.append(f"/ [📂 {part}]({up})")
    return " ".join(crumbs)

def format_dir_index(dir_abs: Path, items: list[Item]) -> str:
    rel_dir = rel(dir_abs) if dir_abs != ROOT else Path()
    title = (rel_dir.name or f"{REPO} index")

    lines = []
    lines.append(f"## {title}")
    lines.append("")
    lines.append(breadcrumbs(rel_dir))
    lines.append("")

    items_sorted = sorted(items, key=lambda e: (not e.is_dir, e.name.lower()))
    for it in items_sorted:
        if it.is_dir:
            href = (it.name + "/") if rel_dir.parts else (rel(it.path).as_posix() + "/")
            lines.append(f"- 📂 [{href}]({href})")
        else:
            p_rel = rel(it.path)
            lines.append(f"- 📄 {it.name}")
            lines.append(f"  - [raw]({raw_url(p_rel)})")
            lines.append(f"  - [github]({blob_url(p_rel)})")

    lines.append("")
    return "\n".join(lines)

# ---------- sitemap & robots ----------
def _url_from_out_path(p: Path) -> str:
    """Map a file under OUT/ to its URL (canonical dir URL for index.html)."""
    rp = rel_out(p).as_posix()
    if rp == "index.html":
        return f"{BASE_URL}/"
    if rp.endswith("/index.html"):
        return f"{BASE_URL}/" + rp[:-10]  # strip 'index.html'
    if p.suffix.lower() == ".html":
        return f"{BASE_URL}/" + rp
    return ""

def build_sitemap_and_robots():
    # Canonical origin: ENV → provenance → BASE_URL
    origin = (os.getenv("BASE_URL") or _canonical_origin_from_provenance() or BASE_URL).rstrip("/")

    def _remap_origin(loc: str) -> str:
        """Replace scheme+host in loc with canonical origin, keep the path."""
        try:
            p = urlparse(loc)
            return f"{origin}{p.path}"
        except Exception:
            return loc

    urls = []
    for path in OUT.rglob("*.html"):
        if path.name.startswith("."):
            continue
        loc = _url_from_out_path(path)
        if not loc:
            continue
        loc = _remap_origin(loc)
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        lastmod = mtime.strftime("%Y-%m-%dT%H:%M:%SZ")
        urls.append((loc, lastmod))

    # de-dup, keep latest lastmod
    seen = {}
    for loc, lastmod in urls:
        if (loc not in seen) or (lastmod > seen[loc]):
            seen[loc] = lastmod

    items = []
    for loc, lastmod in sorted(seen.items()):
        items.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.6</priority>\n"
            "  </url>"
        )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(items) + "\n</urlset>\n"
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {origin}/sitemap.xml\n"
    )
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")

# ---------- RSS ----------
def build_rss_feed():
    """
    Produce /rss.xml with one item per STEM (latest version),
    based on prints/**/provenance.yaml (same schema as PF).
    """
    origin = (os.getenv("BASE_URL") or _canonical_origin_from_provenance() or BASE_URL).rstrip("/")

    prints = ROOT / "prints"
    if not prints.exists():
        return

    by_stem = {}
    for prov in prints.glob("*/*/*/provenance.yaml"):
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        stem = prov.parent.parent.parent.name

        pf_block = data.get("parsed_from_pnpmd") or {}  # old
        title    = (data.get("title") or pf_block.get("title") or stem)
        authors  = normalize_authors(data.get("authors") or pf_block.get("authors"))
        abstract = (data.get("abstract") or pf_block.get("abstract") or "")
        onesent  = (
            data.get("one_sentence_summary")
            or pf_block.get("one_sentence_summary")
            or pf_block.get("one_sentence")
            or ""
        )
        date_norm= (data.get("publication_date") or data.get("creation_date") or pf_block.get("date") or None)
        doi      = (data.get("doi") or (data.get("zenodo") or {}).get("doi") or "")

        # URL: prefer top-level permalink, else stem page
        permalink = (data.get("permalink") or "").strip()
        if permalink and permalink.startswith("http"):
            item_url = permalink.rstrip("/")
        else:
            item_url = f"{origin}/prints/{stem}/"

        dt = _to_datetime(date_norm) or datetime.fromtimestamp(prov.stat().st_mtime)
        keep = by_stem.get(stem)
        if not keep or dt > keep["date"]:
            by_stem[stem] = {
                "stem": stem,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "onesent": onesent,
                "date": dt,
                "url": item_url,
                "doi": doi,
            }

    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title('Preferred Frame Pre-Prints')
    fg.link(href=origin+'/', rel='alternate')
    fg.link(href=origin+'/rss.xml', rel='self')
    fg.description('Latest preprints from Preferred Frame')
    fg.language('en')

    items = sorted(by_stem.values(), key=lambda x: x["date"], reverse=True)
    for it in items:
        fe = fg.add_entry()
        fe.id(it["url"])
        fe.link(href=it["url"])
        fe.title(it["title"])
        desc = it["abstract"] or it["onesent"]
        if desc:
            fe.description(desc)
        for a in it["authors"]:
            nm = a.get("name","").strip()
            if nm:
                fe.author({'name': nm})
        fe.pubDate(it["date"].astimezone(timezone.utc))
        if it["doi"]:
            fe.link(href=f'https://doi.org/{it["doi"].split("/")[-1]}', rel='related')

    rss_xml = fg.rss_str(pretty=True).decode('utf-8')
    (OUT / 'rss.xml').write_text(rss_xml, encoding='utf-8')

# ---------- build ----------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/".nojekyll").write_text("", encoding="utf-8")
    write_cname_if_custom(BASE_URL)

    # --- simple site assets from .scripts/src/site -> site/ ---
    site_src = SRC / "site"
    if site_src.exists():
        for src_path in site_src.rglob("*"):
            if not src_path.is_file():
                continue
            rel_path = src_path.relative_to(site_src)

            if src_path.suffix.lower() == ".md":
                # foo.md -> foo.md.html
                dst_rel = rel_path.with_suffix(rel_path.suffix + ".html")
                dst_path = OUT / dst_rel
                md_body = src_path.read_text(encoding="utf-8")
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                write_html(dst_path, md_body)
            else:
                dst_path = OUT / rel_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)

    # --- root README.md -> site/README.md.html ---
    readme_src = ROOT / "README.md"
    if readme_src.exists():
        dst_path = OUT / "README.md.html"
        md_body = readme_src.read_text(encoding="utf-8")
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        write_html(dst_path, md_body)

    md_body = readme_src.read_text(encoding="utf-8")
    write_html(dst_path, md_body)


    # --- directory indexes over repo tree ---
    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)

        # Never descend into the output site
        if d == OUT:
            dirnames.clear()
            continue

        if dirpath != str(ROOT):
            first = Path(dirpath).relative_to(ROOT).parts[0]
            if first in EXCLUDE_NAMES:
                dirnames.clear()
                continue
            if (Path(dirpath)/"pyvenv.cfg").exists():
                dirnames.clear()
                continue
        prune_dirs(dirpath, dirnames)

        items: list[Item] = []

        for p in sorted([x for x in d.iterdir() if x.is_dir()], key=lambda x: x.name.lower()):
            if p.name in EXCLUDE_NAMES: continue
            if p.name.startswith(".") and p.name != ".well-known": continue
            if (p/"pyvenv.cfg").exists(): continue
            items.append(Item(name=p.name, is_dir=True, mtime=p.stat().st_mtime, path=p))

        for p in sorted([x for x in d.iterdir() if x.is_file() and not x.name.startswith(".")],
                        key=lambda x: x.name.lower()):
            if p.name in EXCLUDE_NAMES: continue
            items.append(Item(name=p.name, is_dir=False, mtime=p.stat().st_mtime, path=p))

        md_body = format_dir_index(d, items)
        out_html = (OUT / rel(d) / "index.html") if d != ROOT else (OUT / "index.html")
        write_md_like_page(out_html, md_body)

    build_sitemap_and_robots()
    build_rss_feed()

if __name__ == "__main__":
    main()
