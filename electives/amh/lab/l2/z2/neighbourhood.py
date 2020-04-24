from typing import List


def SameSizedBlocks(matrix: List[List[int]], matrix_initial):
    """Generate a neighbouring matrix
    """

    i = 0
    while i < n:
        j = 0
        while j < m:
            # take more than k×k size if necessary
            vertical_max = i+k if i+2*k <= n else n
            horizontal_max = j+k if j+2*k <= m else m

            # pick the random value of the block as the flattening value
            # if it's not an allowed one pick the nearest one
            flattening_value = PickTheNearestValueFromList(
                allowed_values,
                matrix_initial[randint(i, vertical_max-1)][randint(j, horizontal_max-1)])

            for g in range(i, vertical_max):
                for h in range(j, horizontal_max):
                    matrix[g][h] = flattening_value
            j += k
        i += k

    return matrix
