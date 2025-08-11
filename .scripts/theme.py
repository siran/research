SITE_TITLE = "An Rodriguez’s documents repository"
SITE_NOTE  = "Files open directly. Click the GitHub icon to view in GitHub."

def header(title, subtitle):
    return f"""<!doctype html>
<meta charset="utf-8">
<title>{title}</title>
<style>
  body{{font:16px/1.55 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}
  h1{{margin:.2rem 0 .25rem}}
  .meta{{opacity:.75;font-size:.9em;margin:.25rem 0 1.25rem}}
  ul{{list-style:none;padding:0}} li{{margin:.25rem 0}} a{{text-decoration:none}} a:hover{{text-decoration:underline}}
  .crumbs a{{opacity:.9}}
  .dirs li::before{{content:"📁 "}} .files li::before{{content:"📄 "}}

  /* README card — same font, subtle emphasis */
  .readme{{background:#faf7ff;border:1px solid #eee;border-left:4px solid #6b46c1;
          border-radius:12px;padding:1rem 1.25rem;box-shadow:0 1px 2px rgba(0,0,0,.04);
          margin:1rem 0 1.25rem}}
  .readme h1,.readme h2,.readme h3{{margin:.2rem 0 .6rem;line-height:1.25}}
  .readme h1{{font-size:1.25em}}
  .readme h2{{font-size:1.15em}}
  .readme h3{{font-size:1.05em}}
  .readme p{{margin:.4rem 0 .8rem}}
  .readme ul, .readme ol{{list-style:disc;padding-left:1.25rem;margin:.25rem 0 .8rem}}
  .readme a{{text-decoration:underline}}
</style>
<h1><a href="/research/">{title}</a></h1>
<div class="meta">{subtitle}</div>
"""


def footer(): return ""
