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
    if tree is None:
        return []

    discovered = [tree, None]

    while len(discovered) > 1:
        # take first element
        current = discovered.pop(0)

        if current is None:
            discovered.append(None)
            continue

        # add its descendants to the discovered pile
        for i in [1, 2]:
            if current[i] is not None:
                discovered.append(current[i])

        yield current[0]


if __name__ == "__main__":

    # generate an arbitrary tree
    tree = generate_tree((0, 100), 4)

    print("tree:", tree)

    print("dfs:", list(tree_walk_dfs(tree)))
    print("bfs:", list(tree_walk_bfs(tree)))
