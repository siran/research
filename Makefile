.PHONY: build serve clean
build:
	python .scripts/build_site.py
serve: build
	python -m http.server -d site 8000
clean:
	rm -rf site
