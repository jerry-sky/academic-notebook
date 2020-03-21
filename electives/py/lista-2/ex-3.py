#!/usr/bin/python3
from sys import argv
import os
from typing import List


def make_all_lowercase(path_):
    """Makes all file and directory names lowercase.

    Recursively searches for files inside provided directory and its
    subdirectories and makes their names lowercase.

    Args:
        `path_`: Directory in which all files and directories will be
            affected.
    """
    # get list of files in current directory
    dir_: List[str] = os.listdir(path_)
    for f in dir_:
        if os.path.isdir(f):
            # change all files in this subdirectory
            make_all_lowercase(path_ + f)
        # make the filename lowercase
        altered = f.lower()
        altered = os.path.join(path_, altered)
        curr = os.path.join(path_, f)
        # make the paths absolute for os.rename to run properly
        curr_abs = os.path.abspath(curr)
        altered_abs = os.path.abspath(altered)

        os.rename(curr_abs, altered_abs)


def main(directory: str):
    """Invokes `make_all_lowercase` function for the provided directory.

    Makes all the file and subdirectory names in the provided directory
    lowercase.

    Args:
        `directory`: The directory in which the function should be run.

    """
    make_all_lowercase(directory)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("usage: ./ex-3.py <directory>")
