#!/usr/bin/python3
from sys import argv
import re


def sum_last_column(file_path: str) -> int:
    """
    Returns a sum of integer values from the last column of each line.

    Takes a value from the last column (a string of characters preceded
    by a whitespace), parses it into integer and returns sum of these
    values.

    Args:
        `file_path`: path to a file from which this function sources
            the data.

    """
    output = 0
    with open(file_path, "r") as file:
        lines = (line for line in file)
        for line in lines:
            val = None
            for val in re.finditer(re.compile(r"\s[0-9]+", re.M), line):
                pass
            if not (val is None):
                output += int(val.group(0))

    return output


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: ./ex-3.py <input_file>")
    else:
        input_file = argv[1]
        print("total bytes:", sum_last_column(input_file))
