
.PHONY: build clean

build: _ex-1-2-3 _ex-4

_ex-1-2-3:
	npx parcel build --public-url . --no-source-maps --dist-dir dist/ex-1-2-3 ex-1-2-3/index.html

_ex-4:
	npx parcel build --public-url . --no-source-maps --dist-dir dist/ex-4 ex-4/index.html

dev:
	npx parcel serve -p 4200 index.html

clean:
	rm -rf .cache .parcel-cache dist
