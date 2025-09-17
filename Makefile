.PHONY: serve clean

serve:
	SITE_BASE=/ python .scripts/build_site.py   # local: root is /
	python -m http.server -d site 8000

clean:
	rm -rf site
