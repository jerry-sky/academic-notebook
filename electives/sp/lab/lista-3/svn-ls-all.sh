#!/bin/bash

function list_files_in_a_directory() {
    # read the first argument — the directory that needs to be listed
    local rev="$1"
    # read the second argument — the revision we’re considering
    local dir="$2"
    # remove the unnecessary slash at the end if it exists
    dir=${dir%/}
    # loop over the files in this directory recursively
    for file in $(svn ls $dir -R -r "$rev"); do
        # if it is not a directory — print out its full path
        if [ "${file: -1}" != "/" ]; then
            printf "$file\n"
        fi
    done
}

list_files_in_a_directory $1 $2
