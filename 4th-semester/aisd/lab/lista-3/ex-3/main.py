#!/usr/bin/python3
from random import randint
import time
import math

COMPARISONS = 0


def binary_search(input_list: list, search_value: int):
    """Search for a value inside the input list.
    """

    global COMPARISONS
    
    # atomic situation O(1)
    if len(input_list) == 1:
        return input_list[0] == search_value
    elif len(input_list) == 0:
        return False

    # pick a pivot in the middle
    pivot_index = len(input_list)//2
    pivot = input_list[pivot_index]

    COMPARISONS += 1
    if pivot <= search_value:
        # pick the higher side
        return binary_search(input_list[pivot_index:], search_value)
    else:  # pivot > search_value:
        # pick the lower side
        return binary_search(input_list[:pivot_index], search_value)


if __name__ == "__main__":

    # collect statistics
    time_stats = []
    comparisons_stats = []

    for n in [1000 * x for x in range(1, 101)]:
        
        l = list(range(0, n))
        # v = l[randint(0, n)]
        v = l[-1]

        # reset the comparisons total count
        COMPARISONS = 0

        begin = time.time()
        result = binary_search(l, v)
        end = time.time()

        time_coefficient = (end-begin) / math.log2(n)
        comparisons_coefficient = COMPARISONS / math.log2(n)

        time_stats.append(time_coefficient)
        comparisons_stats.append(comparisons_coefficient)

    print("O(1) coefficient in terms of time              :",sum(time_stats)/len(time_stats))
    print("O(1) coefficient in terms of comparisons count :",sum(comparisons_stats)/len(comparisons_stats))
