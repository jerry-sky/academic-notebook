from typing import List, Tuple
from random import random, randint
from sys import exit


def PickTheNearestValueFromList(search_list: List[int], search_value) -> int:
    """Picks the nearest value to the provided one.
    """
    return min(search_list, key=lambda x: abs(x - search_value))


def AlterBlockIntensity(
        matrix: List[List[int]], matrix_initial: List[List[int]],
        block_definition: List[List[List[int]]], allowed_values: List[int],
        affect_all_blocks=False) -> None:
    """Generate a neighbouring matrix by changing values of one the matrix's blocks.

    Args:
        `matrix`: The matrix to alter.
        `matrix_initial`: The base input matrix.
        `block_definition`: Defines where the blocks begin.
        `allowed_values`: Defines the values that can be used during rendering.
        `affect_all_blocks`: Whether to alter all blocks or just one random one.
    """

    if affect_all_blocks:
        i = 0
        for row in block_definition:
            j = 0
            for block in row:

                vertical_bound = i + block[0]
                horizontal_bound = j + block[1]

                # pick the random value of the block as the flattening value
                # if it's not an allowed one pick the nearest one
                flattening_value = PickTheNearestValueFromList(
                    allowed_values,
                    matrix_initial[randint(i, vertical_bound-1)][randint(j, horizontal_bound-1)])

                for g in range(i, vertical_bound):
                    for h in range(j, horizontal_bound):
                        matrix[g][h] = flattening_value

                j += block[1]

            i += row[0][0]

    else:

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
    # when resizing only one block you could have a situation when in order
    # to maintain blocks' structural integrity resizing some other blocks
    # would be absolutely necessary; you could have some overlapping or dead
    # zones going on without considering some special cases;
    # to avoid this issue, let's resize a line of blocks instead of just one

    # decide whether to reize horizontally or vertically
    if random() > 0.5:
        # collect all oversized blocks' indexes
        fat_blocks_indexes = []

        for i in range(0, len(block_definition[0])):
            if block_definition[0][i][1] > k:
                fat_blocks_indexes.append(i)

        if len(fat_blocks_indexes) == 0:
            return

        # pick one of them
        line_of_blocks_index = fat_blocks_indexes[randint(
            0, len(fat_blocks_indexes) - 1)]

        # horizontally shrink chosen line of blocks
        for i in range(0, len(block_definition)):
            block_definition[i][line_of_blocks_index][1] -= 1
        # now, choose which neighbouring line to enlarge
        offset = None
        if line_of_blocks_index == len(block_definition[0]) - 1:
            # if the last line was shrunk, enlarge the one to the left
            offset = -1
        elif line_of_blocks_index == 0:
            offset = 1
        else:
            offset = [-1, 1][randint(0, 1)]

        # now, horizontally enlarge neighbouring blocks
        for i in range(0, len(block_definition)):
            block_definition[i][line_of_blocks_index + offset][1] += 1

    else:
        fat_blocks_indexes = []

        for i in range(0, len(block_definition)):
            if block_definition[i][0][0] > k:
                fat_blocks_indexes.append(i)

        if len(fat_blocks_indexes) == 0:
            return

        line_of_blocks_index = fat_blocks_indexes[randint(
            0, len(fat_blocks_indexes) - 1)]

        for i in range(0, len(block_definition[line_of_blocks_index])):
            block_definition[line_of_blocks_index][i][0] -= 1
        offset = None
        if line_of_blocks_index == len(block_definition) - 1:
            offset = -1
        elif line_of_blocks_index == 0:
            offset = 1
        else:
            offset = [-1, 1][randint(0, 1)]
        for i in range(0, len(block_definition[line_of_blocks_index])):
            block_definition[line_of_blocks_index + offset][i][0] += 1

