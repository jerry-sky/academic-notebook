from typing import Iterable


class NeighbourhoodGenerator(object):

    def __init__(self):
        self._all = []
        self._dict = [-1, 0, 1]

    def _recursive(self, start: Iterable, index: int, dimension: int):
        vector = [i for i in start]
        for i in range(0, len(self._dict)):
            copy = [i for i in vector]
            copy[index] = self._dict[i]

            if index == dimension-1:
                self._all.append(copy)
            else:
                self._recursive(copy, index+1, dimension)

    def generate(self, dimension: int = 4):
        start = [0] * dimension
        self._recursive(start, 0, dimension)
        return self._all
