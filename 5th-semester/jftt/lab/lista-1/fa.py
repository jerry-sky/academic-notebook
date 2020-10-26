#!/usr/bin/env python3
from typing import List
from sys import argv, exit, stderr

def suffix_func(x: str, pattern: str) -> int:
    """
    The suffix (\sigma) function that asserts the length of the prefix
    of the `pattern` that is a suffix of the provided string (`x`).
    """
    output = 0
    for k in range(1, len(pattern)+1):
        if x.endswith(pattern[0:k]):
            # it has that suffix
            output = k
    return output


def finite_automaton_matcher(text: str, pattern: str) -> List[int]:
    """
    The main function that finds all occurrences of a pattern in a given string.
    """

    # save the indexes to a list
    output = []

    # starting at q=0 which means no matching pattern has been found yet
    state = 0

    # loop through the whole text
    for i in range(0, len(text)):
        # this is the \delta function that can be defined as a single
        # call to the suffix function
        state = suffix_func(pattern[0:state] + text[i], pattern)

        if state == len(pattern):
            # we’ve reached the final (the only accepting) state
            found_index = i-len(pattern)+1
            output.append(found_index)
            print("found at", found_index, file=stderr)

    return output


if __name__ == "__main__":

    # assert the args
    if len(argv) < 3:
        exit("usage: ./FA <pattern> <filename>")

    pattern = argv[1]
    filename = argv[2]

    # open the file and start the analysis
    with open(filename, "r+") as f:
        contents = f.read()
        results = finite_automaton_matcher(contents, pattern)
        print(results)
