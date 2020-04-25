#!/usr/bin/env python3
from typing import List
from random import randint
from time import time
from sys import exit

# all possible directions the agent can go
DIRECTIONS = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}


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
    if direction == 0:
        position[0] -= 1
    elif direction == 1:
        position[0] += 1
    elif direction == 2:
        position[1] -= 1
    else:
        position[1] += 1


def SimulatedAnnealing(simulation_map: List[List[int]], max_running_time: int):

    # find the agent's position
    agent_position = None
    i = 0
    for row in simulation_map:
        j = 0
        for cell in row:
            if cell == 5:
                agent_position = [i, j]
                break
            j += 1
        if agent_position is not None:
            break
        i += 1

    # pick a random direction
    direction = randint(0, 3)

    solution_current = []

    begin = time()
    end = time()
    while end - begin <= max_running_time:
        surroundings = GetAdjacentCells(*agent_position, simulation_map)

        if 8 in surroundings:
            # found the exit
            solution_current.append(surroundings.index(8))
            break

        if surroundings[direction] == 1:
            # hit the wall -> pick a new direction
            candidate_directions = list(filter(
                lambda x: x != direction, range(0, 4)))
            direction = candidate_directions[randint(0, 2)]
            continue

        # continue walking
        solution_current.append(direction)
        TranslatePosition(agent_position, direction)

        end = time()

    return solution_current



if __name__ == "__main__":

    t, n, m = map(lambda x: int(x), input().split())

    simulation_map = []
    for i in range(0, n):
        simulation_map.append(
            list(map(lambda x: int(x), list(input())))
        )

    solution = SimulatedAnnealing(simulation_map, t)

    for step in solution:
        print(DIRECTIONS[step], end="")
