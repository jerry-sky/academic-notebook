
.PHONY: css css-compressed

css:
	./compile-css.sh

css-compressed:
	./compile-css.sh 1

css-compressed-prefix:
	./compile-css.sh 1 1

css-dev:
	./sass -w css

sass:
	./download-sass.sh

clean:
	rm -rf css/*.css* minified sass
