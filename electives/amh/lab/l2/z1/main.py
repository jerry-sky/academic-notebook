#!/usr/bin/env python3
from typing import Tuple
from functools import reduce
from math import sqrt, cos, exp, pi as PI
from time import time
from random import random
from sys import exit
from neighbourhood import NeighbourhoodGenerator


def SalomonFunc(x: Tuple[float]) -> float:

    x_length = sqrt(reduce(
        lambda so_far, curr: so_far + curr**2,
        x,
        0
    ))

    return 1 - cos(2*PI*x_length) + 0.1 * x_length


def RandomMove(original_pos: Tuple[float], jump_size: float, dimensions=4) -> Tuple[float]:
    """Moves a provided position vector in a random fashion.

    Generates a random value from a range of [-1; 1] * jump_size and
    adds it to the originally provided vector.
    """

    direction = []
    for i in range(0, dimensions):
        direction.append(
            original_pos[i]
            + ((random()*2 - 1) * jump_size))

    return tuple(direction)


def Probability(difference: float, temperature: float) -> float:
    return exp(-0.001*difference/temperature)
    # very poor results actually (even while tweaking the c constant):
    # return 1.0 / (1.0 + exp(0.000001*difference/temperature))


def SimulatedAnnealing(solution_initial: Tuple[float], temperature_initial: float, running_time_max: int, jump_size_initial: float, jump_size_min: float = 0.1):
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
    jump_size = jump_size_initial

    generator = NeighbourhoodGenerator()
    offsets = generator.generate()

    begin = time()
    end = time()
    while end - begin <= running_time_max and temperature_current > 0:

        for offset in offsets:
            # scan the neighbouring points
            # below is the old way — take only one vector at a time which gives
            # very low probability of finding the best solution
            ## solution_candidate = RandomMove(solution_current, jump_size)

            # multiply the offset vector by the jump_size coefficient
            solution_candidate = list(map(lambda x: random() * x * jump_size, offset))
            for i in range(0,4):
                solution_candidate[i] += solution_current[i]
            solution_candidate_value = SalomonFunc(solution_candidate)
            # print(solution_candidate)

            if solution_current_value > solution_candidate_value:
                # the candidate was just plainly better
                solution_current = solution_candidate
                solution_current_value = solution_candidate_value

                temperature_current *= 0.99
            else:
                difference = abs(solution_candidate_value -
                                 solution_current_value)

                if Probability(difference, temperature_current) > random():
                    # candidate solution wasn't better but it got lucky
                    solution_current = solution_candidate
                    solution_current_value = solution_candidate_value
                    # jump_size = jump_size_initial

        # temperature_current = temperature_current/(10 * temperature_current + 1)

        end = time()

    return solution_current, solution_current_value


if __name__ == "__main__":

    # read the input numbers
    t, x1, x2, x3, x4 = map(lambda x: int(x), input().split())
    # compose the start point
    x = (x1, x2, x3, x4)
    # run the algorithm
    solution, solution_value = SimulatedAnnealing(
        x, 50, t, jump_size_initial=2, jump_size_min=0.1)
    # print out the results
    for i in solution:
        print(i, end=" ")
    print(solution_value, end="")

