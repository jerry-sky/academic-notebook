#!/usr/bin/env python3
from typing import List
from copy import deepcopy
from math import exp
from sys import exit, stderr
from time import time
from random import random, randint


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


def PickTheNearestValueFromList(search_list: List[int], search_value) -> int:
    """Picks the nearest value to the provided one.
    """
    return min(search_list, key=lambda x: abs(x - search_value))


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
    # defines blocks sizes
    solution_current_block_definition = []

    temperature_current = temperature_initial

    begin = time()
    end = time()
    while end-begin <= running_time_max and temperature_current > 0:

        solution_candidate = deepcopy(solution_current)
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
                        solution_candidate[g][h] = flattening_value
                j += k
            i += k

        solution_candidate_value = MatrixDistance(
            matrix_initial, solution_candidate)

        if solution_current_value > solution_candidate_value:
            # the solution was plainly better
            solution_current = solution_candidate
            solution_current_value = solution_candidate_value
            temperature_current *= 0.7
        else:
            difference = abs(solution_candidate_value - solution_current_value)

            # print("probability", Probability(difference, temperature_current))

            if Probability(difference, temperature_current) > random():
                # candidate solution wasn't better but it got lucky
                solution_current = solution_candidate
                solution_current_value = solution_candidate_value
        end = time()

    return solution_current


def PrintMatrix(matrix: List[List[int]], file=stderr) -> None:

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

    PrintMatrix(matrix_initial)

    print(MatrixDistance(matrix_initial, matrix_output))

    PrintMatrix(matrix_output)
