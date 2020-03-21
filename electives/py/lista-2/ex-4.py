#!/usr/bin/python3
from sys import argv
import os
import hashlib
from typing import List, Set


def _hash(x: str):
    """Shorthand for the hash function."""
    return hashlib.sha512(x.encode()).hexdigest()


def _pj(x: str, y: str):
    """Shorthand for `os.path.join`."""
    return os.path.join(x, y)


def _gs(x: str):
    """Shorthand for `os.path.getsize`."""
    return os.path.getsize(x)


def check_for_duplicate_files(directory: str):
    """Find files of duplicate content.

    Find all files that are the same in content and of the same size.

    Args:
        `directory`: Path to the directory in which the search is going
        to be run.

    """
    # get all files in the current directory
    paths_ = list(os.walk(directory))
    # collect all the duplicates in a set
    output: Set[List[str]] = set()

    for path in paths_:
        files: List[str] = path[2]
        dir_: str = path[0]
        # iterate over all files in the directory
        for path_cur in files:
            duplicates: List[str] = []
            with open(_pj(dir_, path_cur)) as cur_file:
                # get file's size and contents' hash
                cur_contents = cur_file.read()
                cur_hash = _hash(cur_contents)
                cur_size = _gs(_pj(dir_, path_cur))
                # iterate over the same list of files to
                # search for duplicates
                for path_dup in paths_:
                    files_dup: List[str] = path_dup[2]
                    dir_sub: str = path_dup[0]
                    for file_dup in files_dup:
                        with open(_pj(dir_sub, file_dup)) as dup_file:
                            # get file's size and contents' hash
                            dup_contents = dup_file.read()
                            dup_hash = _hash(dup_contents)
                            dup_size = _gs(_pj(dir_sub, file_dup))
                            # check size and contents hash
                            if dup_size == cur_size and dup_hash == cur_hash:
                                duplicates.append(_pj(dir_sub, file_dup))
            output.add(tuple(duplicates))

    return tuple(filter(lambda x: len(x) > 1, output))


def main(directory: str):
    """Invokes `check_for_duplicate_files` function for the provided
    directory.
    """
    divider = "----------------------"
    duplicates = check_for_duplicate_files(directory)
    for duplicate in duplicates:
        print(divider)
        for file_ in duplicate:
            print(file_)
    print(divider)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("usage: ./ex-4.py <directory>")
