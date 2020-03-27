#!/usr/bin/python3
from typing import List


def quick_sort(to_sort: List[any]):
    """Uses QuickSort algorithm to sort elements.
    """
    # simply return if the provided list is atomic
    if len(to_sort) < 2:
        return to_sort
    # pick a pivot
    pivot = to_sort[0]
    # divide the list with the pivot in the middle
    smaller = list(filter(lambda x: x < pivot, to_sort))
    bigger = list(filter(lambda x: x > pivot, to_sort))
    # count how many times the pivot element has appeared
    # we need to check for that as not to loose data
    copies = sum(1 for x in to_sort if x == pivot)

    return [
        elem
        for sublist in [quick_sort(smaller), [pivot] * copies, quick_sort(bigger)]
        for elem in sublist
    ]


if __name__ == "__main__":
    input_list = list(
        map(int, input("provide a list of integers to quick-sort: ").split())
    )
    print(quick_sort(input_list))
