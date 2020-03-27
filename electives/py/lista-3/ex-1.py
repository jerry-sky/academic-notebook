#!/usr/bin/python3
from typing import List
from functools import reduce
from sys import argv


def transpose(matrix: List[str]):
    """Transposes a matrix.
    """
    output: List[str] = ["" for _ in range(0, len(matrix))]

    for row in matrix:
        values = row.split()
        i = 0
        for val in values:
            output[i] = " ".join(filter(lambda x: len(x) > 0, [output[i], val]))
            i += 1

    return output


def transpose_alt(matrix: List[str]):
    """Transposes a matrix.

    Transposes a matrix in a more geeky way as it uses a long one-liner.
    *(It's a one-liner metaphorically speaking of course as for
    readability reasons it's been split up into multiple lines.)*

    """
    return [
        reduce(
            lambda so_far, curr: " ".join([so_far, curr.split()[i]]), matrix, "",
        ).lstrip()
        for i in range(0, len(matrix))
    ]


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage ./ex-1.py <input_file>")
    else:
        input_file = argv[1]
        with open(input_file, "r") as inp:
            matrix: List[str] = []
            for line in inp:
                if len(line) > 0:
                    matrix.append(line)
            print(transpose_alt(matrix))
