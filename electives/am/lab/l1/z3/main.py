#!/usr/bin/python3
import time
from random import randint
from typing import List, Tuple

POSSIBLE_DIRECTION = ["U", "D", "R", "L"]


def isInverse(a, b) -> bool:
    """Check if two provided directions are the opposites of each other.
  """
    if (a == "L" and b == "R") or (a == "R" and b == "L"):
        return True
    if (a == "U" and b == "D") or (a == "D" and b == "U"):
        return True

    return False


def getRoomMapValue(
    map_: List[List[int]], position, offset_direction: POSSIBLE_DIRECTION = ""
) -> int:
    """Get the cell value from the room map.

    Optional argument `offset_direction` is for looking up the cell next
    to the requested one in the desired direction.
    """
    # apply the offset if provided
    offset = [0, 0]
    if offset_direction != "":
        movePos(offset, offset_direction)

    return map_[position[0] + offset[0]][position[1] + offset[1]]


def movePos(pos: List[int], direction: POSSIBLE_DIRECTION):
    """Translate provided position by one in the desired direction.
    """
    if direction == POSSIBLE_DIRECTION[0]:
        pos[0] -= 1
    elif direction == POSSIBLE_DIRECTION[1]:
        pos[0] += 1
    elif direction == POSSIBLE_DIRECTION[2]:
        pos[1] += 1
    elif direction == POSSIBLE_DIRECTION[3]:
        pos[1] -= 1


def getSurroundings(pos, map_):
    """Get map values of surrounding cells.

    Returns a list of cell values adhering to the order of
    the `POSSIBLE_DIRECTION` list.
    """
    output = []
    for d in POSSIBLE_DIRECTION:
        output.append(getRoomMapValue(map_, pos, d))
    return output


def getSolutionNeighbourhood(input_solution):
    """Get all the neighbouring step sequences of a solution.
    """

    forbidden_swaps: List[Tuple[int]] = []
    neighbourhood: List[List[POSSIBLE_DIRECTION]] = []

    for i in range(0, len(input_solution)):
        for j in range(0, len(input_solution)):
            neighbour = list(input_solution)
            if (i, j) in forbidden_swaps:
                continue
            forbidden_swaps.append((i, j))
            # swap two agent moves
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            # remove unnecessary mini-loops such as LR or UD
            length = len(neighbour)
            i = 0
            while i < length - 1:
                curr = neighbour[i]
                next_ = neighbour[i + 1]
                if isInverse(curr, next_):
                    del neighbour[i]
                    del neighbour[i]
                    i -= 2
                    if i < 0:
                        i = -1
                    length -= 2
                i += 1

            neighbourhood.append(neighbour)

    return neighbourhood


def validateSolution(solution, starting_position, map_) -> List[str]:
    """Validates solution and gives a shorter version of it if possible.

    It returns None if the solution is not valid.
    """
    pos = list(starting_position)
    modified_solution = []
    for move in solution:
        current_cell = getRoomMapValue(map_, pos)
        # check if we've hit a wall
        if current_cell == 1:
            return None
        # check if we're already at the exit
        elif current_cell == 8:
            return modified_solution
        movePos(pos, move)
        modified_solution.append(move)
    if getRoomMapValue(map_, pos) == 8:
        return modified_solution
    else:
        return None


def main():
    # ignore the `m` parameter
    t, n, _ = map(lambda x: int(x), input().split())
    # just to be sure we have enough time for exiting the loops
    # and printing a solution

    # parse the input data
    room_map: List[List[int]] = []
    starting_position: Tuple[int] = ()
    for i in range(0, n):
        row = list(map(lambda x: int(x), list(input())))
        # save agent's starting position
        if 5 in row:
            starting_position = (i, row.index(5))
        room_map.append(row)

    # measure time
    start_time = time.time()
    now_time = time.time()

    currentSolution = []

    # current position
    agent_position = list(starting_position)
    agent_surroundings = getSurroundings(agent_position, room_map)

    # pick a random direction
    direction = POSSIBLE_DIRECTION[randint(0, 3)]

    if 1 not in agent_surroundings and 8 not in agent_surroundings:
        # we're not at a wall already

        # go a step until you hit a wall or an exit
        while not getRoomMapValue(room_map, agent_position, direction) in (8, 1):
            currentSolution.append(direction)
            movePos(agent_position, direction)

    if 8 in agent_surroundings:
        # pure luck - we are already at the exit
        direction = POSSIBLE_DIRECTION[agent_surroundings.index(8)]
        currentSolution.append(direction)
        return (currentSolution, len(currentSolution))

    # now we need to complete our base solution by finding the exit
    previousDirection = ""
    while now_time - start_time <= t:
        # check if we're already near the exit
        agent_surroundings = getSurroundings(agent_position, room_map)
        if 8 in agent_surroundings:
            direction = POSSIBLE_DIRECTION[agent_surroundings.index(8)]
            currentSolution.append(direction)
            break
        # otherwise pick a direction and go for it
        for i in range(0, 4):
            # chose a direction
            cell = agent_surroundings[i]
            if cell == 0:
                direction = POSSIBLE_DIRECTION[i]
                # if the picked direction is the inverse of the previous one,
                # pick another one to avoid infinite loops
                if isInverse(direction, previousDirection):
                    continue
                # go until you hit another wall
                while getRoomMapValue(room_map, agent_position, direction) != 1:
                    agent_surroundings = getSurroundings(agent_position, room_map)
                    if 8 in agent_surroundings:
                        break
                    movePos(agent_position, direction)
                    currentSolution.append(direction)
                previousDirection = direction
                break
        now_time = time.time()

    # now we have a base solution, time for TabuSearch

    while now_time - start_time <= t:
        # generate neighbourhood
        neighbourhood = getSolutionNeighbourhood(currentSolution)
        for neighbour in neighbourhood:
            # validate the neighbour solution
            validatedNeighbour = validateSolution(
                neighbour, starting_position, room_map
            )
            # f(x) = \infty
            if validatedNeighbour is None:
                continue
            # found a better solution
            elif len(validatedNeighbour) < len(currentSolution):
                currentSolution = validatedNeighbour
        now_time = time.time()

    return (currentSolution, len(currentSolution))


if __name__ == "__main__":

    solution, steps = main()
    print(steps)
    list(map(lambda x: print(x, end=""), solution))
