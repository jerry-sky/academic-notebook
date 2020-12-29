#!/usr/bin/python3
from typing import List
from functools import reduce


def powerset(master_set: List):
    """Returns a Powerset of the provided set.
    """
    return map(
        lambda x: set(x),
        reduce(
            lambda so_far, curr: [subset + [curr] for subset in so_far] + so_far,
            master_set,
            [[]],
        ),
    )


if __name__ == "__main__":
    input_set = input("provide a set: ").split()
    print("Powerset:", list(powerset(input_set)))
