#!/usr/bin/env python3
from xsyang_func import XSYang
from typing import Iterable
from random import random
from time import time
from sys import exit
from copy import deepcopy

FLOAT_PRECISION = 24


def is_vector_zero(vector: Iterable[float]) -> bool:
    """Verifies whether the vector in question is \overline0.
    """

    for i in range(0, len(vector)):
        if round(vector[i], FLOAT_PRECISION) != 0:
            return False

    return True


def particle_swarm_func_minimum(func, initial_solution: Iterable[float], pop_size: int,
                                breaking_cft: float, own_best_cft: float, global_best_cft: float,
                                initial_max_speed: float, max_running_time: int):
    """Finds the global minimum of a function using Particle Swarm Optimization technique.
    """

    begin = time()

    # define the dimension the vectors are in
    dimension = len(initial_solution)

    # all the particles in the swarm...
    swarm = [initial_solution]
    # ... their best solutions ...
    swarm_best = [(initial_solution, func(initial_solution))]
    # ... and their current speeds
    swarm_speed = []
    # generate the speeds
    for i in range(0, pop_size):
        swarm_speed.append(
            [
                (random()-0.5) * 2 * initial_max_speed for _ in range(dimension)
            ]
        )
    # and generate the rest of the particles
    for i in range(1, pop_size):
        swarm.append(
            [
                initial_solution[d] + swarm_speed[i][d] for d in range(dimension)
            ]
        )
        swarm_best.append(deepcopy((swarm[i], func(swarm[i]))))

    # before iterating, establish the best solution so far
    swarm_the_best = deepcopy(swarm_best[0])
    for i in range(1, pop_size):
        if swarm_the_best[1] > swarm_best[i][1]:
            swarm_the_best = deepcopy(swarm_best[i])

    end = time()
    while end-begin <= max_running_time:

        # count those particles that have stopped
        zero_speed_particles = 0

        for i in range(0, pop_size):
            curr_speed = swarm_speed[i]
            if not is_vector_zero(curr_speed):

                curr = (swarm[i], func(swarm[i]))
                curr_best = swarm_best[i]

                # move the particle
                for d in range(0, dimension):

                    beta = random() * own_best_cft
                    eta = random() * global_best_cft

                    curr_speed[d] = breaking_cft * curr_speed[d] + beta * \
                        (curr_best[0][d] - curr[0][d]) + \
                        eta * (swarm_the_best[0][d] - curr[0][d])

                    curr[0][d] += curr_speed[d]

                curr = (swarm[i], func(swarm[i]))

                # analyse the current solution after performing movement
                if curr[1] < curr_best[1]:
                    swarm_best[i] = deepcopy(curr)
                if curr[1] < swarm_the_best[1]:
                    swarm_the_best = deepcopy(curr)

            else:
                # count the particle as non-moving
                zero_speed_particles += 1

        if zero_speed_particles == pop_size:
            # all particles have settled down
            break

        end = time()

    return swarm_the_best


if __name__ == "__main__":

    inp = input().split()

    if len(inp) < 11:
        exit('too few arguments given')

    t = int(inp[0])

    initial_solution = list(map(
        lambda x: float(x), inp[1:6]
    ))

    epsilon = list(map(
        lambda x: float(x), inp[6:11]
    ))

    def wrapper_func(x: Iterable[float]):
        return XSYang(x, epsilon)

    results = particle_swarm_func_minimum(
        wrapper_func, initial_solution,
        pop_size=100, breaking_cft=0.8, own_best_cft=0.7,
        global_best_cft=0.9, initial_max_speed=0.9, max_running_time=t
    )

    solution = list(map(
        lambda x: round(x, FLOAT_PRECISION),
        results[0]
    ))
    solution_value = round(results[1], FLOAT_PRECISION)

    print(*solution, solution_value)
