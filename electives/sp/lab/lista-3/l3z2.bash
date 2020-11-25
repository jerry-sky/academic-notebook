#!/bin/bash

# create an associative array to store the statistics
declare -A stats

rev="$1"
dir="$2"

# loop over every file in the directory
for file in $(./svn-ls-all.sh "$rev" "$dir"); do
    # loop over every word in the current file
    for word in $(svn cat $dir$file -r "$rev"); do
        if [ ${stats["$word"]+yup} ]; then
            # if the word is already in the array — increase its occurrences by one
            ((stats['$word']++))
        else
            # otherwise save it as a new word
            ((stats['$word']=1))
        fi
    done
done

# print the stats
for word in "${!stats[@]}"; do
    printf -- "\033[38;5;45mthe word ‘\033[0m$word\033[38;5;45m’ appeared ${stats[$word]} time(s)\033[0m\n"
done

