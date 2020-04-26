#!/usr/bin/env python3
from typing import List
from copy import deepcopy
from math import exp, floor
from sys import stderr
from time import time
from random import random, randint
from neighbourhood import AlterBlockIntensity, AlterBlockSizes


def MatrixDistance(one: List[List[int]], two: List[List[int]]) -> float:
    n = len(one)
    m = len(one[0])
    if n != len(two) or m != len(two[0]):
        raise Exception('matrices don\'t have same sizes')

    output = 0

    for i in range(0, n):
        for j in range(0, m):
            output += (one[i][j] - two[i][j])**2

    return output / n / m


def Probability(difference: float, temperature: float) -> float:
    return exp(-(0.1 ** 10)*difference/temperature)


def SimulatedAnnealing(
        matrix_initial: List[List[int]],
        allowed_values: List[int],
        n: int, m: int, k: int,
        temperature_initial: float, running_time_max: int):

    # we're dividing the output matrix into at least k×k sized blocks
    # of numbers that are equal and if it is impossible to insert another
    # block we're making it bigger enough to fit into the matrix

    # generate first output matrix with k×k sized blocks with values
    # based on the first element of each block
    solution_current = [[allowed_values[0]] * m for _ in range(0, n)]
    solution_current_value = MatrixDistance(solution_current, matrix_initial)

    # define blocks' sizes
    solution_current_block_definition = []
    i = 0
    while i <= n-k:
        solution_current_block_definition.append([])
        j = 0
        while j <= m-k:
            # enlarge the last blocks
            vert = k if i + 2*k <= n else n - i
            horiz = k if j + 2*k <= m else m - j
            solution_current_block_definition[-1].append([vert, horiz])
            j += k
        i += k

    temperature_current = temperature_initial

    begin = time()
    end = time()
    while end-begin <= running_time_max and temperature_current > 0:

        solution_candidate = deepcopy(solution_current)
        solution_candidate_block_definition = deepcopy(solution_current_block_definition)

        if random() > 0.8:
            # alter the block structure
            AlterBlockSizes(solution_candidate_block_definition, k)
            # rebuild the matrix
            AlterBlockIntensity(solution_candidate, matrix_initial, solution_candidate_block_definition, allowed_values, True)
        else:
            # alter just one block
            AlterBlockIntensity(solution_candidate, matrix_initial, solution_candidate_block_definition, allowed_values)

        solution_candidate_value = MatrixDistance(
            matrix_initial, solution_candidate)

        if solution_current_value > solution_candidate_value:
            # the solution was plainly better
            solution_current = solution_candidate
            solution_current_value = solution_candidate_value
            solution_current_block_definition = solution_candidate_block_definition

            temperature_current *= 0.7
        else:
            difference = abs(solution_candidate_value - solution_current_value)

            if Probability(difference, temperature_current) > random():
                # candidate solution wasn't better but it got lucky
                solution_current = solution_candidate
                solution_current_value = solution_candidate_value
                solution_current_block_definition = solution_candidate_block_definition
        end = time()

    return solution_current


def PrintMatrix(matrix: List[List[int]], file=stderr) -> None:
    """Pretty-prints the provided matrix.
    """

    for row in matrix:
        for el in row:
            el_str = str(el)
            print(el_str, " " * (3-len(el_str)), end=" ", file=file)
        print(file=file)


if __name__ == "__main__":

    allowed_values = [0, 32, 64, 128, 160, 192, 223, 255]

    # collect input data
    t, n, m, k = map(lambda x: int(x), input().split())

    matrix_initial = []
    for i in range(0, n):
        matrix_initial.append(
            list(map(lambda x: int(x), input().split()))
        )

    matrix_output = SimulatedAnnealing(
        matrix_initial, allowed_values, n, m, k, 50, t)

    print(MatrixDistance(matrix_initial, matrix_output))

    PrintMatrix(matrix_output)
