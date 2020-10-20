#!/bin/bash

function list_files_in_a_directory() {
    # read the first argument — the directory that needs to be listed
    local dir="$1"
    # remove the unnecessary slash at the end if it exists
    dir=${dir%/}
    # loop over the files in this directory
    for file in $dir/*; do
        # if it is a regular file — print out its name
        if [ -f "$file" ]; then
            printf "$file\n"
        # if it is a directory — recursively call this function
        elif [ -d "$file" ]; then
            list_files_in_a_directory "$file"
        fi
    done
}

list_files_in_a_directory $1
