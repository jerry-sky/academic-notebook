#!/usr/bin/python3
from typing import List, Tuple
from random import randint


class Node(object):
    """Atomic construct that allows building node trees.
    """

    def __init__(self, value: any):
        self._children: List = []
        self._value: any = value

    @property
    def children(self) -> List:
        """Gets all node's descendants.
        """
        return self._children

    @property
    def value(self) -> any:
        """Gets the value of this node.
        """
        return self._value

    def add_child(self, child):
        """Adds a new node as a child of this node.
        """
        self._children.append(child)

    @staticmethod
    def generate_arbitrary_tree(
            value_range: Tuple[int], max_children: int, height: int):
        """Generates an arbitrary tree containing integer values.

        Args:
            `value_range`: Range to use when choosing a random integer
                value for a node.
            `max_children`: How many children a node can have.
            `height`: Desired height of the node tree.
        """

        if height == 0:
            return None

        value = randint(*value_range)
        tree = Node(value)

        if height > 1 and max_children > 0:
            # generate node's children
            children_count = randint(1, max_children)
            for i in range(0, children_count):
                tree.add_child(
                    Node.generate_arbitrary_tree(
                        value_range, max_children, height-1
                    )
                )

        return tree

    @staticmethod
    def tree_walk_dfs(tree):
        """Generates a tree walk DFS-style.
        """

        yield tree.value

        for child in tree.children:
            yield from Node.tree_walk_dfs(child)

    @staticmethod
    def tree_walk_bfs(tree):
        """Generates a tree walk BFS-style.
        """
        if tree is None:
            return []

        discovered = [tree, None]

        while len(discovered) > 1:
            current = discovered.pop(0)

            if current is None:
                discovered.append(None)
                continue

            for child in current.children:
                if child is not None:
                    discovered.append(child)

            yield current.value


if __name__ == "__main__":
    tree = Node.generate_arbitrary_tree((0, 100), 4, 4)

    print(list(Node.tree_walk_dfs(tree)))
    print(list(Node.tree_walk_bfs(tree)))
