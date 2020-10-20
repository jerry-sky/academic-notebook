#/bin/bash

# record all words
declare -A stats

dir="$1"

# loop over every file in the directory
for file in $(./ex-1.sh $dir); do
    # keep track of which words have been already recorded in the current file
    declare -A current_file
    # loop over every word in the current file
    for word in $(cat $file); do
        if [ ! ${current_file["$word"]+yup} ]; then
            # if the word has not been already found in the current file — save it
            if [ ${stats["$word"]+yup} ]; then
                # if the word is already in the array — increase its occurrences by one
                ((stats['$word']++))
            else
                # otherwise save it as a new word
                ((stats['$word']=1))
            fi
            # flag that word as it was found in the current file
            current_file["$word"]="a"
        fi
    done
    unset current_file
done

# print the stats
for word in "${!stats[@]}"; do
    printf -- "\033[38;5;45mthe word ‘\033[0m$word\033[38;5;45m’ \033[38;5;45mappeared in ${stats[$word]} file(s)\033[0m\n"
done

