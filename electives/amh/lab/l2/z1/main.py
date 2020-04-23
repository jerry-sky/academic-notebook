#!/usr/bin/env python3
from typing import Tuple
from functools import reduce
from math import sqrt, cos, exp, pi as PI
from time import time
from random import random


def SalomonFunc(x: Tuple[float]) -> float:

    x_length = sqrt(reduce(
        lambda so_far, curr: so_far + curr**2,
        x,
        0
    ))

    return 1 - cos(2*PI*x_length) + 0.1 * x_length


def RandomMove(original_pos: Tuple[float], jump_size: float, dimensions=4) -> Tuple[float]:
    """Moves a provided position vector in a random fashion.

    Generates a random value from a range of [-1; 1] and adds it to the
    originally provided vector.
    """

    direction = []
    for i in range(0, dimensions):
        direction.append(
            original_pos[i]
            + ((random()*2 - 1) * jump_size))

    return tuple(direction)


def Probability(difference: float, temperature: float) -> float:
    return exp(-0.001*difference/temperature)
    # return 1.0 / (1.0 + exp(0.000001*difference/temperature)) # very poor results actually


def SimulatedAnnealing(solution_initial: Tuple[float], temperature_initial: float, running_time_max: int, jump_size: float, jump_size_min: float = 0.1):
    """Finds minimum of a Salomon function using simulated annealing algorithm.

    Args:
        `solution_initial`: The point in 4D space from which the algorithm
        starts its search.
        `temperature_initial`: Initial annealing temperature.
        `running_time_max`: Abort searching after that amount of time
        unless temperature got to 0 first.
        `jump_size`: The length of the vector that will be randomly selected
        during searching for better (or worse) solutions.

    """

    solution_current = solution_initial
    solution_current_value = SalomonFunc(solution_current)
    temperature_current = temperature_initial

    solution_best = solution_current
    solution_best_value = solution_current_value

    begin = time()
    end = time()
    while end - begin <= running_time_max and temperature_current > 0:
        # move the current solution in a random direction
        solution_candidate = RandomMove(solution_current, jump_size)
        solution_candidate_value = SalomonFunc(solution_candidate)

        if solution_best_value > solution_candidate_value:
            solution_best = solution_candidate
            solution_best_value = solution_candidate_value

        if solution_current_value > solution_candidate_value:
            # the candidate was just plainly better
            solution_current = solution_candidate
            solution_current_value = solution_candidate_value
        else:
            difference = abs(solution_candidate_value - solution_current_value)

            if Probability(difference, temperature_current) > random():
                solution_current = solution_candidate
                solution_current_value = solution_candidate_value

        # temperature_current = temperature_current/(10 * temperature_current + 1)
        temperature_current *= 0.99
        # jump_size *= 0.9999999
        # if jump_size < jump_size_min:
        #     jump_size = jump_size_min

        end = time()

    if solution_best_value < solution_current_value:
        return solution_best, solution_best_value
    else:
        return solution_current, solution_current_value


if __name__ == "__main__":
    # print(SimulatedAnnealing((10, 3, -5, 15), 50,
    #                          10, jump_size=0.7, jump_size_min=0.1))
    print(SimulatedAnnealing((1, 2, 3, 4), 50,
                             10, jump_size=0.7, jump_size_min=0.1))
    # print(SimulatedAnnealing((0,0,0,0), 100, 5, jump_size=0.7))
