#!/bin/bash

archive="sass.tar.gz"

# download Sass
curl -L --output "$archive" 'https://github.com/sass/dart-sass/releases/download/1.34.0/dart-sass-1.34.0-linux-x64.tar.gz'

# unpack it
tar -x 'dart-sass/sass' --strip-components=1 -f "$archive"

# remove the archive
rm "$archive"
