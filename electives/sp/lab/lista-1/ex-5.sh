#!/bin/bash

dir="$1"

for file in $(./ex-1.sh "$dir"); do
    cat "$file" | tr a A > /tmp/.temporary-ex-5
    rm "$file"
    mv /tmp/.temporary-ex-5 "$file"
done
