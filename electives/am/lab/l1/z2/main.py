#!/usr/bin/python3
import random
import time
from typing import List, Tuple


def generateNeighbourhood(cities):
    """Generates all 2-opt permutations of `cities` with respect to TabuSearch.

    This function doesn't touch the first and the last city to preserve
    the natural TSP cycle.
    """
    forbidden_swaps: List[Tuple] = []
    neighbourhood: List[List[int]] = []
    for i in range(1, len(cities) - 1):
        for j in range(i, len(cities) - 1):
            neighbour = list(cities)
            if (neighbour[i], neighbour[j]) in forbidden_swaps:
                continue
            forbidden_swaps.append((neighbour[i], neighbour[j]))
            # swap two cities
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbourhood.append(neighbour)
    return neighbourhood


def main():
    # first collect the data
    t, n = map(lambda x: int(x), input().split())
    distances = []

    for i in range(0, n):
        tmp = list(map(lambda x: int(x), input().split()))
        distances.append(tmp)

    currentSolution = [0]
    currentSolutionCost = 0

    startTime = time.time()
    nowTime = time.time()
    i = 0
    # choose a random path
    while len(currentSolution) < n:
        city = random.randint(0, n - 1)
        while city in currentSolution:
            city = random.randint(0, n - 1)
        currentSolution.append(city)
        currentSolutionCost += distances[currentSolution[i]][currentSolution[i + 1]]
        i += 1
    # add the last step which is to get back to the starting city
    currentSolution.append(0)
    currentSolutionCost += distances[currentSolution[-2]][currentSolution[-1]]

    while nowTime - startTime <= t:
        neighbourhood = generateNeighbourhood(currentSolution)
        for neighbour in neighbourhood:
            neighbourCost = 0
            for city in range(0, n):
                neighbourCost += distances[neighbour[city]][neighbour[city + 1]]
            if neighbourCost < currentSolutionCost:
                currentSolution = neighbour
                currentSolutionCost = neighbourCost
        nowTime = time.time()

    print(currentSolutionCost)
    list(map(lambda x: print(x+1, end=" "), currentSolution))


if __name__ == "__main__":
    main()
