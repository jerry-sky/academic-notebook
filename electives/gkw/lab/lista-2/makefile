
.PHONY: build clean

base_make = npx parcel build --public-url .

build:
	 $(base_make) ex-1/index.html --dist-dir dist/ex-1
	 $(base_make) ex-2/index.html --dist-dir dist/ex-2
	 $(base_make) ex-3-4/index.html --dist-dir dist/ex-3-4
	 cp index.html dist/index.html

dev:
	npx parcel serve -p 4200 index.html

clean:
	rm -rf .cache .parcel-cache dist
