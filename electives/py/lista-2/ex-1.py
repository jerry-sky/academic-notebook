#!/usr/bin/python3
from sys import argv
import re


def summarize_file(file_path):
    """Summarizes the provided file by some basic measurements.

    Returns:
        A tuple containing how many (bytes, words, lines it contains,
        and what is the maximum character count in one line).

    """
    if file_path is None:
        return

    bytes_ = 0
    words = 0
    lines = 1
    max_line_width = 0
    with open(file_path) as file:
        for line_ in file:
            # enforce string type
            line: str = line_
            if len(line) > max_line_width:
                max_line_width = len(line)
            lines += 1
            words += len(line.split())
            bytes_ += len(line.encode())
    return (bytes_, words, lines, max_line_width)


def main(file_path: str):
    """Invokes `summarize_file` to get the basic file information.

    Prints the output of `summarize_file` - a summary of a file from
    the provided filepath. Tells how many bytes, words, and lines and
    what is the max line width of the file.

    """

    bytes_, words, lines, max_line_width = summarize_file(file_path)

    print("bytes          :", bytes_)
    print("words          :", words)
    print("lines          :", lines)
    print("max line width :", max_line_width)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("usage: ./ex-1.py <file_path>")
