#!/usr/bin/python3
from random import randint


def generate_tree(label_range, height):
    """Generates a binary tree of provided height.

    Args:
        `label_range`: Range of numbers from which the binary tree node
            labels should be generated.
        `height`: Desired height of the binary tree.

    """
    if height == 0:
        return None

    return [
        randint(*label_range),
        generate_tree(label_range, height-1),
        generate_tree(label_range, height-1)
    ]


def tree_walk_dfs(tree):
    """Generates a binary tree walk DFS-style.
    """
    yield tree[0]

    if tree[1] is not None:
        yield from tree_walk_dfs(tree[1])
    if tree[2] is not None:
        yield from tree_walk_dfs(tree[2])


def tree_walk_bfs(tree):
    """Generates a binary tree walk BFS-style.
    """
    height = tree_height(tree)
    for i in range(0, height):
        yield from get_tree_values_level(tree, i)


def get_tree_values_level(tree, level):
    """Gets all values from a particular level of a tree.
    """
    if tree is None:
        return
    if level == 0:
        yield tree[0]
    else:
        yield from get_tree_values_level(tree[1], level-1)
        yield from get_tree_values_level(tree[2], level-1)


def tree_height(tree):
    """Returns tree height.
    """
    if tree is None:
        return 0
    left = tree_height(tree[1])
    right = tree_height(tree[2])
    if left > right:
        return left + 1
    else:
        return right + 1


if __name__ == "__main__":

    # generate an arbitrary tree
    tree = generate_tree((0, 100), 4)

    print(tree)

    print(list(tree_walk_dfs(tree)))
    print(list(tree_walk_bfs(tree)))
