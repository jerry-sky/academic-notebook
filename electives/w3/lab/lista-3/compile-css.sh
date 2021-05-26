#!/bin/bash

# compress output
args=""
if [ -n "$1" ]; then
    args="--style compressed"
fi

# output CSS to different directory
if [ -n "$2" ]; then
    prefix="minified/"
fi

for f in $(ls css/[!_]*.scss); do
    name="${f%.*}"
    ./sass "$f" $prefix"$name".css $args
done
