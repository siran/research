SITE_TITLE = "An Rodriguez’s documents repository"
SITE_NOTE  = "Files open directly. Click the GitHub icon to view in GitHub."

def header(title, subtitle):
    return f"""<!doctype html>
<meta charset="utf-8">
<title>{title}</title>
<style>
 body{{font:16px/1.55 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}
 h1{{margin:.2rem 0 .25rem}} .meta{{opacity:.75;font-size:.9em;margin:.25rem 0 1.25rem}}
 ul{{list-style:none;padding:0}} li{{margin:.25rem 0}} a{{text-decoration:none}} a:hover{{text-decoration:underline}}
 .crumbs a{{opacity:.9}} .dirs li::before{{content:"📁 "}} .files li::before{{content:"📄 "}}
 .readme{{margin:1rem 0 1.25rem}}
</style>
<h1><a href="/research/">{title}</a></h1>
<div class="meta">{subtitle}</div>
"""
def footer(): return ""
