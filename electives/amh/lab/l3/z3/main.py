#!/usr/bin/env python3
from sys import stderr, exit
from typing import Iterable
from time import time
from random import random, randint

# all possible directions the agent can go
DIRECTIONS = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
INVERSED_DIRECTIONS = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

INFINITY = float('inf')


def is_inverse(a, b) -> bool:
    """Checks if two provided directions are the opposites of each other.
    """
    if (a == 2 and b == 3) or (a == 3 and b == 2):
        return True
    if (a == 0 and b == 1) or (a == 1 and b == 0):
        return True

    return False


def remove_mini_loops(solution: Iterable[int]) -> None:
    """Removes unnecessary mini loops like LR or UD from the solution.
    """
    length = len(solution)
    i = 0
    while i < length - 1:
        cur = solution[i]
        nex = solution[i + 1]
        if is_inverse(cur, nex):
            del solution[i]
            del solution[i]
            i -= 2
            if i < 0:
                i = -1
            length -= 2
        i += 1


def translate_position(position: Iterable[int], direction) -> None:
    """Moves provided vector in the provided direction.
    """
    if direction == 0:
        position[0] -= 1
    elif direction == 1:
        position[0] += 1
    elif direction == 2:
        position[1] -= 1
    else:
        position[1] += 1


def validate_solution(
        solution: Iterable[int], starting_position,
        simulation_map: Iterable[Iterable[int]]) -> Iterable[int]:
    """Validates solution and gives a shorter version of it if possible.

    It returns `None` if the solution is not valid.
    """
    pos = list(starting_position)
    modified_solution = []
    for move in solution:
        current_cell = simulation_map[pos[0]][pos[1]]
        # check if the agent hit a wall
        if current_cell == 1:
            return None
        # check if the agent is already at the exit
        elif current_cell == 8:
            return modified_solution
        translate_position(pos, move)
        modified_solution.append(move)

    if simulation_map[pos[0]][pos[1]] == 8:
        return modified_solution
    else:
        return None


def fitness_func(population, starting_position, simulation_map):
    population = map(
        lambda sol: validate_solution(
            sol, starting_position, simulation_map) if sol is not None else None,
        population
    )
    # sort the population by their fitness
    population = sorted(population, key=lambda sol: len(sol)
                        if sol is not None else INFINITY)
    return population


def GA_find_shortest_path(simulation_map: Iterable[Iterable[int]], initial_solutions: Iterable[int],
                          max_pop_size: int, mutation_probability: float, max_running_time: int):

    begin = time()

    starting_position = None
    i = 0
    for line in simulation_map:
        j = 0
        for cell in line:
            if cell == 5:
                starting_position = (i, j)
            j += 1
        i += 1

    # the first population
    population = [*initial_solutions]

    # now, we perform the GA
    end = time()
    while end-begin <= max_running_time:

        # selection stage
        pivot = round(max_pop_size/2)
        # select the best solutions based on their length (the lowest the best)
        founding_fathers = population[:pivot]
        the_rest = population[pivot:]
        # take a valid solution that wasn't that good but it will
        # introduce more diversity
        if len(population) == max_pop_size:
            r = None
            while r is None and len(the_rest) > 0:
                r = the_rest.pop(randint(0, len(the_rest)-1))
            if r is not None:
                founding_fathers.append(r)


        # crossover stage
        population = [*founding_fathers]
        # generate remaining population members based on the „founding fathers”
        while len(population) < max_pop_size:
            # pick two parents to crossover
            p_one = founding_fathers.pop(randint(0, len(founding_fathers)-1))
            p_two = founding_fathers[randint(0, len(founding_fathers)-1)]
            founding_fathers.append(p_one)
            # take a part from the first parent
            index = randint(1, len(p_one)-1)
            part_one = p_one[:index]
            if random() > 0.5:
                part_one = p_one[index:]
            # take a part from the second parent
            index = randint(1, len(p_two)-1)
            part_two = p_two[index:]
            if random() > 0.5:
                part_two = p_two[:index]

            new_member = part_one + part_two

            # mutation stage
            for i in range(0, len(new_member)):
                if random() > 1-mutation_probability:
                    new_member[i] = (new_member[i] + randint(0, 3)) % 4

            population.append(new_member)

        # fitness stage

        # all solutions that are invalid are `None`s
        # not only are we evaluating the solutions but we're trimming out parts that are
        # unnecessary – meaning if the agent got to the solution earlier than the length
        # of the solution in question, we're leaving out the remaining part thus creating
        # an even better solution (a shorter solution)
        population = fitness_func(
            population, starting_position, simulation_map)

        end = time()

    return population[0]


if __name__ == '__main__':

    t, n, _, s, p = map(lambda x: int(x), input().split())

    simulation_map = []
    for _ in range(0, n):
        simulation_map.append(
            list(map(lambda x: int(x), list(input())))
        )

    initial_solutions = []

    for _ in range(0, s):
        sol = list(input())
        sol_processed = []
        for move in sol:
            sol_processed.append(INVERSED_DIRECTIONS[move])
        initial_solutions.append(sol_processed)

    result = GA_find_shortest_path(simulation_map, initial_solutions, max_pop_size=p,
                                   mutation_probability=0.05,
                                   max_running_time=t)

    for r in result:
        print(DIRECTIONS[r], end='', file=stderr)

    print(len(result))
