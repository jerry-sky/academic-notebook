#/bin/bash

# word → files with occurrences of that word
declare -A words_files

dir="$1"

# loop over every file in the directory
for file in $(./ex-1.sh $dir); do
    # keep track of which words have been already recorded in the current file
    declare -A current_file
    # loop over every word in current file
    for word in $(cat $file); do
        if [ ! ${current_file["$word"]+yup} ]; then
            # if the word has not been already found in the current file — save the name of the file
            words_files["$word"]+=" $file"
            # flag that word as it was found in the current file
            current_file["$word"]="a"
        fi
    done
    unset current_file
done

# print all words with their occurrences in files
for word in "${!words_files[@]}"; do
    printf -- "\033[38;5;45mthe word ‘\033[0m$word\033[38;5;45m’ \033[38;5;45mappeared in:\033[0m\n"
    for file in ${words_files["$word"]}; do
        printf "    \033[38;5;81ma file named ‘\033[0m$file\033[38;5;81m’:\033[0m\n"
        # look for occurrences with `grep`
        # (indents all the output with `sed`)
        grep -w -- "$word" "$file" | sed 's/^/    /'
        # printf -- "    \033[38;5;81;3mfile end\033[0m\n"
    done
    printf "\n"
done

