
.PHONY: build clean

build: _ex-1-2-3 _ex-4 _ex-5

_ex-1-2-3:
	npx parcel build --public-url . --dist-dir dist/ex-1-2-3 ex-1-2-3/index.html

_ex-4:
	npx parcel build --public-url . --dist-dir dist/ex-4 ex-4/index.html

_ex-5:
	npx parcel build --public-url . --dist-dir dist/ex-5 ex-5/index.html

dev:
	npx parcel serve -p 4200 index.html

clean:
	rm -rf .cache .parcel-cache dist
