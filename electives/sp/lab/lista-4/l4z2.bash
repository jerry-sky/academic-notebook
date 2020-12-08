#!/bin/bash

rev1="$1"
rev2="$2"

svn_dir="$3"

# extract the directory name
dir=${svn_dir%/}
dir="${dir##*/}"

# initialize an empty git repository
git init "$dir"

cd "$dir"

# inside the newly created git repository we can iteratively apply all the changes
for r in $(seq $rev1 $rev2); do

    # check if given revision exists
    svn log -q -r "$r" "$svn_dir"
    if [ $? == "1" ]; then
        # revision doesn’t exist — skip
        continue
    fi

    # copy the svn directory at that revision
    rm -rf *
    svn export --force -q "$svn_dir" -r "$r" "./"

    # extract the commit message of that revision
    msg="$(svn log -r $r $svn_dir | tail -n +4 | head -n -2)"

    # commit these change in the new git repository
    git add "./**/*"
    git commit -m "$msg"

done
