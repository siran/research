.PHONY: serve clean

serve:
	python .scripts/build_site.py
	python -m http.server -d site 8000

clean:
	rm -rf site
