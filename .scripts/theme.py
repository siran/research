# --- Site text ---
SITE_TITLE = "An Rodriguez’s documents repository"
SITE_NOTE  = "Files open directly. Click the GitHub icon to view in GitHub."

def header(display_h1: str, subtitle: str, title_tag: str) -> str:
    return f"""<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_tag}</title>
<style>
  :root {{
    --text:#222; --muted:#6b7280; --border:#e5e7eb; --bg:#fff; --link:#1a5fff;
  }}
  *{{box-sizing:border-box}}
  body{{color:var(--text);background:var(--bg);font:16px/1.55 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}
  h1{{margin:.2rem 0 .25rem;font-weight:700}}
  h1 a{{color:inherit;text-decoration:none}} h1 a:hover{{text-decoration:underline}}
  .meta{{color:var(--muted);font-size:.9em;margin:.25rem 0 1.25rem}}
  a{{color:var(--link);text-decoration:none}} a:hover{{text-decoration:underline}}
  ul{{list-style:none;padding:0;margin:0}} li{{margin:.25rem 0}}
  .crumbs a{{opacity:.9}}
  .dirs li::before{{content:"📁 "}} .files li::before{{content:"📄 "}}
  .switcher{{margin:.25rem 0 .5rem;color:var(--muted);font-size:.95em}}
  .switcher a{{color:inherit}} .switcher strong{{color:#000}}
  /* README card */
  .readme{{border:1px solid var(--border);border-radius:8px;padding:1rem 1.25rem;margin:1rem 0 1.25rem;background:#fff}}
  .readme h1,.readme h2,.readme h3{{margin:.2rem 0 .6rem;line-height:1.25}}
  .readme h1{{font-size:1.25em}} .readme h2{{font-size:1.15em}} .readme h3{{font-size:1.05em}}
  .readme p{{margin:.4rem 0 .8rem}}
  .readme ul,.readme ol{{list-style:disc;padding-left:1.25rem;margin:.25rem 0 .8rem}}
  .readme a{{text-decoration:underline}}
  .readme code{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.95em}}
  img.gh-icon{{height:1em;vertical-align:middle;opacity:.85;border:none}} img.gh-icon:hover{{opacity:1}}
</style>
<h1>{display_h1}</h1>
<div class="meta">{subtitle}</div>
"""

def footer() -> str:
    return ""
