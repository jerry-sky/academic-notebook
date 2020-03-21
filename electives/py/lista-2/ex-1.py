#!/usr/bin/python3
from sys import argv
import re


def summarize_file(file_path):
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

    bytes_, words, lines, max_line_width = summarize_file(file_path)

    print("bytes", bytes_)
    print("words", words)
    print("lines", lines)
    print("max line width", max_line_width)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("usage: ./ex-1.py file_path")
