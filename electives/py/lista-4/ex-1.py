#!/usr/bin/python3
import time
from random import randint


def example_function(*args):
    output = 1
    for i in range(0, 100000):
        factor = args[randint(0, len(args)-1)]
        if factor == 0:
            output *= randint(0, 100)
        else:
            output *= factor
    return output


def running_time(func):
    """Prints measured running time of a function."""

    begin = time.time()

    def func_(*args, **kwargs):
        output = func(*args, **kwargs)
        end = time.time()
        print("function", func.__name__, "ran for", (end - begin), "seconds")
        return output
    return func_


if __name__ == "__main__":
    @running_time
    def test_func():
        return example_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    test_func()
