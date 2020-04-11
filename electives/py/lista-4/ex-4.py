#!/usr/bin/python3
from inspect import getfullargspec
import math


class _overload_storage(object):
    """Storage for overloaded functions.

    Attributes:
        `_functions`: Static dictionary that holds all overloaded
            functions indexed by function name.
        `_func_name`: Name of the function that is overloaded.

    """
    _functions = {}
    _func_name = ""

    def __init__(self, func):

        # take not of the function name
        self._func_name = func.__name__

        # if there is no entry for that function name add an empty list
        # for it
        if _overload_storage._functions.get(self._func_name) is None:
            _overload_storage._functions[self._func_name] = []

        # add new overload of this function
        _overload_storage._functions[self._func_name].append(
            {
                # save all args of this overload for identification
                'args': getfullargspec(func).args,
                # the actual function to run
                'func': func
            }
        )

    def __call__(self, *args, **kwargs):
        """Overwrites the default call function to make this class
        „callable” to enable function overloading.
        """

        for f in _overload_storage._functions[self._func_name]:
            # loop over all overloads of this function
            args_count = len(args) + len(kwargs)

            if args_count != len(f['args']):
                continue

            return f['func'](*args, **kwargs)

        # it may be replaced with `raise`
        return None


def overload(func):
    """Make an overload of a function.
    """
    c = _overload_storage(func)
    return c


if __name__ == "__main__":
    @overload
    def norm(a, b):
        return math.sqrt(a*a + b*b)

    @overload
    def norm(a, b, c):
        return abs(a) + abs(b) + abs(c)

    # testing if another function with the same argument count doesn't
    # interfere with other overloaded functions
    @overload
    def another_one(a, b):
        return a + b

    print(
        norm(2, 4),
        norm(2, 3, 4),
        another_one(2, 4),
        sep="\n"
    )
