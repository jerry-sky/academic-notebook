#!/usr/bin/python3
from typing import List, Tuple, Union
from sys import argv
import json

def flatten(list: Union[List, Tuple]):
    """Flattens a list of lists.

    Unwraps all the elements trapped inside the master list or all other
    sublists contained inside the master list.

    """
    for elem in list:
        if isinstance(elem, List) or isinstance(elem, Tuple):
            yield from flatten(elem)
        else:
            yield elem


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage ./ex-2.py <input_file in json format>")
    else:
        input_file = argv[1]
        with open(input_file, "r") as inp:
            inp_contents = inp.read()
            master_list: List[any] = json.loads(inp_contents)
            print(list(flatten(master_list)))
