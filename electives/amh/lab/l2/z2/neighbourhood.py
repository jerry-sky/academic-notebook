from typing import List, Tuple
from random import random, randint


def PickTheNearestValueFromList(search_list: List[int], search_value) -> int:
    """Picks the nearest value to the provided one.
    """
    return min(search_list, key=lambda x: abs(x - search_value))


def AlterBlockIntensity(
        matrix: List[List[int]], matrix_initial: List[List[int]],
        block_definition: List[List[List[int]]], allowed_values: List[int]) -> None:
    """Generate a neighbouring matrix by changing values of one the matrix's blocks.

    Args:
        `matrix`: The matrix to alter.
        `matrix_initial`: The base input matrix.
        `block_definition`: Defines where the blocks begin.
    """

    # # pick a random block
    block_index_x = randint(0, len(block_definition) - 1)
    block_index_y = randint(0, len(block_definition[block_index_x]) - 1)

    # render the actual indexes of the matrix block
    i = 0
    j = 0
    for a in range(block_index_x):
        i += block_definition[a][block_index_y][0]
    for a in range(block_index_y):
        j += block_definition[block_index_x][a][1]

    # current block's size
    block_size = block_definition[block_index_x][block_index_y]

    vertical_bound = i + block_size[0]
    horizontal_bound = j + block_size[1]

    # pick the random value of the block as the flattening value
    # if it's not an allowed one pick the nearest one
    flattening_value = PickTheNearestValueFromList(
        allowed_values,
        matrix_initial[randint(i, vertical_bound-1)][randint(j, horizontal_bound-1)])

    for g in range(i, vertical_bound):
        for h in range(j, horizontal_bound):
            matrix[g][h] = flattening_value


def AlterBlockSizes(block_definition: List[List[List[int]]], k: int) -> None:
    """Generate a neighbouring matrix by adjusting the blocks' sizes.
    """

    # collect all oversized blocks' indexes
    fat_blocks_indexes = []
    i = 0
    for row in block_definition:
        j = 0
        for block in row:
            if block[0] > k or block[1] > k:
                fat_blocks_indexes.append((i, j))
            j += 1
        i += 1

    if len(fat_blocks_indexes) == 0:
        return

    # pick one of them
    block_indexes = fat_blocks_indexes[randint(0, len(fat_blocks_indexes) - 1)]

    ###
