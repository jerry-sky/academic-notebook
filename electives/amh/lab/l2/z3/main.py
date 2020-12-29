#!/usr/bin/env python3
from typing import List
from random import randint, shuffle, random
from time import time
from sys import exit, stderr
from math import exp
# from numpy import random as num

# all possible directions the agent can go
DIRECTIONS = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}


def IsInverse(a, b) -> bool:
    """Checks if two provided directions are the opposites of each other.
    """
    if (a == 2 and b == 3) or (a == 3 and b == 2):
        return True
    if (a == 0 and b == 1) or (a == 1 and b == 0):
        return True

    return False


def InvertDirection(direction: int) -> int:
    """Returns the opposite direction to the one given.
    """
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    else:
        return 2


def RemoveMiniLoops(solution: List[int]) -> None:
    """Removes unnecessary mini loops like LR or UD from the solution.
    """
    length = len(solution)
    i = 0
    while i < length - 1:
        cur = solution[i]
        nex = solution[i + 1]
        if IsInverse(cur, nex):
            del solution[i]
            del solution[i]
            i -= 2
            if i < 0:
                i = -1
            length -= 2
        i += 1


def GetAdjacentCells(x: int, y: int, simulation_map: List[List[int]]) -> List[int]:
    """Get values from the cells that surround the provided cell.
    """
    output = []

    # generate the surroundings in the order of the `DIRECTIONS` array
    # namely, 0 -> Up -> output[0] is the cell's value that is above provided position
    for i in [-1, 1]:
        output.append(simulation_map[x + i][y])
    for i in [-1, 1]:
        output.append(simulation_map[x][y + i])

    return output


def TranslatePosition(position: List[int], direction) -> None:
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


def Probability(difference: float, temperature: float) -> float:
    return exp(-(0.1 ** 0)*difference/temperature)


def ValidateSolution(
        solution: List[int], starting_position,
        simulation_map: List[List[int]]) -> List[int]:
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
        TranslatePosition(pos, move)
        modified_solution.append(move)

    if simulation_map[pos[0]][pos[1]] == 8:
        return modified_solution
    else:
        return None


def SimulatedAnnealing(
        simulation_map: List[List[int]],
        temperature_initial: float, max_running_time: int):

    # find the agent's position
    starting_position = None
    i = 0
    for row in simulation_map:
        j = 0
        for cell in row:
            if cell == 5:
                starting_position = [i, j]
                break
            j += 1
        if starting_position is not None:
            break
        i += 1

    # now we need to establish the base solution by choosing random
    # directions and going for them until we find the exit

    # pick a random direction
    direction = randint(0, 3)

    solution_current = []

    position_current = list(starting_position)

    begin = time()
    end = time()
    while end - begin <= max_running_time:
        surroundings = GetAdjacentCells(
            position_current[0], position_current[1], simulation_map)

        if 8 in surroundings:
            # found the exit
            solution_current.append(surroundings.index(8))
            break

        if surroundings[direction] == 1:
            # generate directions that will lead to hitting a wall
            # avoid coming back the same way
            forbidden_directions = [InvertDirection(direction)]
            # forbidden_directions = []
            for i in range(0, 4):
                if surroundings[i] == 1:
                    forbidden_directions.append(i)
            # hit the wall -> pick a new direction
            candidate_directions = list(filter(
                lambda x: x not in forbidden_directions, range(0, 4)))
            direction = candidate_directions[randint(
                0, len(candidate_directions)-1)]
            continue

        # continue walking
        solution_current.append(direction)
        TranslatePosition(position_current, direction)

        end = time()

    RemoveMiniLoops(solution_current)

    # now with this base solution, we can search for a better one

    temperature_current = temperature_initial

    while end - begin <= max_running_time and temperature_current > 0.1 ** 2:

        solution_candidate = list(solution_current)
        # apply random permutation
        # solution_candidate = list(num.permutation(solution_candidate))
        shuffle(solution_candidate)

        # for some reason we need to check the time now, otherwise the program
        # will just disregard the time constraint and run much longer that it
        # was told to
        end = time()
        if end - begin > max_running_time:
            break

        # remove unnecessary mini loops like LR or UD
        RemoveMiniLoops(solution_candidate)

        solution_candidate = ValidateSolution(
            solution_candidate, starting_position, simulation_map)

        if solution_candidate is None:
            # ignore invalid solutions
            continue

        if len(solution_candidate) == len(solution_current):
            # solution resulting in the same
            temperature_current *= 0.8
        if len(solution_candidate) < len(solution_current):
            # solution was plainly better
            solution_current = solution_candidate
            temperature_current *= 0.7
        else:
            difference = abs(len(solution_candidate) - len(solution_current))

            if Probability(difference, temperature_current) > random():
                # solution wasn't better but it got lucky
                solution_current = solution_candidate

        end = time()

    return solution_current


if __name__ == "__main__":

    # read input data
    t, n, m = map(lambda x: int(x), input().split())

    simulation_map = []
    for i in range(0, n):
        simulation_map.append(
            list(map(lambda x: int(x), list(input())))
        )

    solution = SimulatedAnnealing(simulation_map, 60, t)

    # last little touches
    RemoveMiniLoops(solution)

    # print the solution
    print(len(solution))

    for step in solution:
        print(DIRECTIONS[step], end="", file=stderr)
