#!/usr/bin/env python3
from collections import namedtuple
from typing import Iterable, Any
from sys import exit, stdin

# define the node used in the priority queue
PQNode = namedtuple('PQNode', ['key', 'priority'])


def parent(index: int) -> int:
    """Gets parent's index.
    """
    return index // 2


def left(index: int) -> int:
    """Gets left descendant's index.
    """
    return 2 * index


def right(index: int) -> int:
    """Gets right descendant's index.
    """
    return 2 * index + 1


class PriorityQueue(object):
    """
    Basic implementation of the Priority Queue data structure.

    Lower `priority` integer value the higher priority some element gets.
    """

    def __init__(self, raw: Iterable[Any] = []):
        self.__heap = raw
        # build heap
        n = len(raw)-1
        # for i \gets \lfloor n/2 \rfloor to 0
        # n//2 to 0 inclusive; step=-1
        for i in range(n//2, -1, -1):
            self.__heapify(i)

    @property
    def heap(self):
        return self.__heap

    def __heapify(self, index):
        """Repairs the heap.
        """
        heap = self.__heap
        # check if the heap characteristic still holds
        # A[i] \ge A[parent(i)]
        tmp = [index, left(index), right(index)]
        tmp = list(filter(lambda x: x < len(heap), tmp))
        tmp_priorities = list(map(lambda x: self.__heap[x].priority, tmp))
        # pick the index of the lowest priority item
        x = tmp[tmp_priorities.index(min(tmp_priorities))]

        if x != index:
            # characteristic does not hold - repair the heap
            heap[index], heap[x] = heap[x], heap[index]
            self.__heapify(x)

    def insert(self, key: int, priority: int) -> None:
        """Inserts `key` value with a priority of `priority`.
        """
        # create the new node to insert
        new_node = PQNode(key=key, priority=priority)
        # append it as the last leaf in the tree
        heap = self.__heap
        heap.append((key, priority))
        i = len(heap)-1
        # run sort of „reverse-heapify” if it's not the first element to be inserted
        if i != -1:
            # reverse back up the tree if neccessary
            while i > 0 and heap[parent(i)].priority > new_node.priority:
                heap[i] = heap[parent(i)]
                i = parent(i)
        # insert the node where it is appropriate
        heap[i] = new_node

    def __delete_at_index(self, index: int) -> PQNode:
        """Deletes the element at `index`.
        """
        heap = self.__heap
        # keep the PQNode we're removing
        output = heap[index]
        # place the last element in place of the element we're removing
        heap[index] = heap[-1]
        # remove the last item
        del heap[-1]
        if not self.is_empty and index != len(heap):
            # fix the heap
            self.__heapify(index)

        return output

    @property
    def is_empty(self) -> bool:
        """Returns a predicate stating whether the PQ is empty or not.
        """
        return len(self.__heap) == 0

    @property
    def top(self) -> PQNode:
        """Returns the highest priority node.
        """
        return self.__heap[0]

    def pop(self) -> PQNode:
        """Pops the highest priority node.
        """
        return self.__delete_at_index(0)

    def bottom_bound_flatten_priority(self, key: int, min_priority: int) -> None:
        """Sets a new priority for elements of a given key if their
        current priority is lower then `min_priority`.
        """
        heap = self.__heap

        # count how many of these nodes have to be altered
        count = 0

        length = len(heap)
        i = 0
        while i < length:
            if heap[i].key == key and heap[i].priority > min_priority:
                # found a PQNode with sought key
                count += 1
                # delete it
                self.__delete_at_index(i)
                # reset the search, because the heap was restructured
                # so the sought elements may have changed their places
                i = -1
                length -= 1
            i += 1

        for _ in range(count):
            self.insert(key, min_priority)


if __name__ == "__main__":

    # operation count
    M = input()
    try:
        M = int(M)
    except ValueError:
        exit('first line must contain an integer')

    PQ = PriorityQueue()

    operation_count = 0
    for line in stdin:
        operation_count += 1
        if operation_count >= M:
            break

        # parse given operation data
        raw_data = line.split()
        operation = raw_data[0]
        data = raw_data[1:]
        try:
            data = [int(x) for x in data]
        except ValueError:
            exit('given data needs to be a tuple of integers')

        if operation == 'insert' and len(data) >= 2:
            # insert given key with a given priority
            key = data[0]
            priority = data[1]

            PQ.insert(key, priority)

        elif operation == 'empty':
            print('1' if PQ.is_empty else '0')

        elif operation == 'top':
            if PQ.is_empty:
                print()
            else:
                print(PQ.top.key)

        elif operation == 'pop':
            if PQ.is_empty:
                print()
            else:
                print(PQ.pop().key)

        elif operation == 'priority' and len(data) >= 2:
            key = data[0]
            min_priority = data[1]
            PQ.bottom_bound_flatten_priority(key, min_priority)

        elif operation == 'print':
            for node in PQ.heap:
                print(
                    '(' + str(node.key) + ', '
                    + str(node.priority) + ')'
                )
