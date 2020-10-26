#!/usr/bin/env python3
from typing import List
from sys import exit, stderr, argv


def compute_prefix_func(pattern: str) -> List[int]:
    """
    Renders the so called ‘prefix function’ that is a map of
    the pattern to search for.
    """
    m = len(pattern)
    pi = [0 for _ in range(0, m)]
    k = 0
    for state in range(1, m):
        while k > 0 and pattern[k] != pattern[state]:
            k = pi[k]
        if pattern[k] == pattern[state]:
            k += 1
        pi[state] = k

    return pi


def kmp_matcher(text: str, pattern: str) -> List[int]:
    """
    Finds all occurrences of a given pattern in a given string using
    the Knuth-Morris-Pratt algorithm.
    """

    # save the indexes to a list
    output = []

    # prepare the pattern map
    pi = compute_prefix_func(pattern)

    # state represents the number of characters matched currently
    state = 0
    for i in range(0, len(text)):

        while state > 0 and pattern[state] != text[i]:
            # the next character doesn’t match
            state = pi[state-1]

        if pattern[state] == text[i]:
            # the next character matches
            state += 1

        if state == len(pattern):
            # we’ve reached the final (the only accepting) state
            found_index = i-len(pattern)+1
            output.append(found_index)
            print("found at", found_index, file=stderr)
            # search for potential new matches
            state = pi[state-1]

    return output


if __name__ == "__main__":

    # assert the args
    if len(argv) < 3:
        exit("usage: ./KMP <pattern> <filename>")

    pattern = argv[1]
    filename = argv[2]

    # open the file and start the analysis
    with open(filename, "r+") as f:
        contents = f.read()
        results = kmp_matcher(contents, pattern)
        print(results)
