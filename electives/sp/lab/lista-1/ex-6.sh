#!/bin/bash

dir="$1"

for file in $(./ex-1.sh $dir); do
    while read -- line; do
        declare -A stats
        for word in $line; do
            if [ "${stats[$word]}" = 'first' ]; then
                # the word has occurred for the second time
                printf "\033[38;5;45mthe word ‘\033[0m$word\033[38;5;45m’ occurred more than once in a file called ‘\033[0m$file\033[38;5;45m’ on the following line:\033[0m\n    $line\n"
                stats["$word"]="second"
            elif [ "${stats['$word']}" = '' ]; then
                # the word has never occurred before
                stats["$word"]="first"
            fi
        done
        unset stats
    done <"$file"
done
