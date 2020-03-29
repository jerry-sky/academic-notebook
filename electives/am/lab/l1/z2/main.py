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

    current_solution = [0]
    current_solution_cost = 0

    start_time = time.time()
    now_time = time.time()
    i = 0

    # choose a local-minimum path
    while len(current_solution) < n:
        # distances from the current city to all the other
        current_distances = distances[current_solution[i]]
        # pick the smallest distance
        lowest_cost = max(current_distances)
        lowest_cost_city = current_distances.index(lowest_cost)
        j = 0
        for dist in current_distances:
            if (
                j not in current_solution
                and j != current_solution[i]
                and lowest_cost > dist
            ):
                lowest_cost = dist
                lowest_cost_city = j
            j += 1
        # add the city to the current solution
        current_solution.append(lowest_cost_city)
        current_solution_cost += current_distances[current_solution[i + 1]]
        i += 1
    # add the last step which is to get back to the starting city
    current_solution.append(0)
    current_solution_cost += distances[current_solution[-2]][current_solution[-1]]

    # use TabuSearch to further improve chosen solution
    while now_time - start_time <= t:
        neighbourhood = generateNeighbourhood(current_solution)
        for neighbour in neighbourhood:
            neighbour_cost = 0
            for j in range(0, n):
                neighbour_cost += distances[neighbour[j]][neighbour[j + 1]]
            if neighbour_cost < current_solution_cost:
                current_solution = neighbour
                current_solution_cost = neighbour_cost
        now_time = time.time()

    return (current_solution, current_solution_cost)


if __name__ == "__main__":
    solution, cost = main()
    print(cost)
    list(map(lambda x: print(x, end=" "), solution))
