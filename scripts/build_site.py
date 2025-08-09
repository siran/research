#!/usr/bin/env python3
import os, shutil, html, urllib.parse

ROOT = "."
OUT  = "site"   # temp build dir that Pages will deploy

def hidden(name): return name.startswith(".") or name == ".gitignore"
def relpath(p):  return os.path.relpath(p, ROOT)
def outpath(p):  return os.path.join(OUT, relpath(p))

def write_index(dir_out, entries, show_parent):
    lines = ["<!doctype html><meta charset='utf-8'><body><ul>"]
    if show_parent: lines.append('<li><a href="../">../</a></li>')
    # dirs first, then files
    for name, isdir in sorted(entries, key=lambda x: (not x[1], x[0].lower())):
        href = urllib.parse.quote(name) + ("/" if isdir else "")
        label = html.escape(name + ("/" if isdir else ""))
        lines.append(f'<li><a href="{href}">{label}</a></li>')
    lines.append("</ul></body>")
    with open(os.path.join(dir_out, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# clean/build OUT
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)

for dirpath, dirs, files in os.walk(ROOT):
    # prune hidden dirs and the OUT dir itself
    dirs[:] = [d for d in dirs if not hidden(d) and os.path.join(dirpath,d) != os.path.abspath(OUT)]
    if relpath(dirpath).startswith(".."):  # safety
        continue
    cur_out = outpath(dirpath)
    os.makedirs(cur_out, exist_ok=True)

    # copy files (non-hidden)
    entries = []
    for f in files:
        if hidden(f): continue
        src = os.path.join(dirpath, f)
        dst = os.path.join(cur_out, f)
        shutil.copy2(src, dst)
        entries.append((f, False))

    # collect subdirs (already pruned)
    for d in dirs:
        os.makedirs(os.path.join(cur_out, d), exist_ok=True)
        entries.append((d, True))

    # write index.html
    rel = relpath(dirpath)
    write_index(cur_out, entries, show_parent=(rel != "."))

print(f"Built static site in ./{OUT}")