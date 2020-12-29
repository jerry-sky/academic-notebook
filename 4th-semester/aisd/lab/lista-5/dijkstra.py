#!/usr/bin/env python3
from collections import namedtuple
from graph import Graph, INFINITY
from priority_queue import PriorityQueue, PQNode
from sys import exit, stdin, stderr
from time import time
from graph_input_utility import read_graph_definition

DijkstraAlgorithmResult = namedtuple(
    'DijkstraAlgorithmResult', ['dist', 'prev'])


def Dijkstra_algorithm(graph: Graph, starting_node: int) -> DijkstraAlgorithmResult:

    dist = [INFINITY for _ in range(graph.nodes_count)]
    prev = [None for _ in range(graph.nodes_count)]

    dist[starting_node] = 0
    prev[starting_node] = starting_node

    # prepare list of tuples of nodes labels with their starting distances
    dist_nodes = [
        PQNode(key=i, priority=dist[i])
        for i in range(0, graph.nodes_count)
    ]

    Q = PriorityQueue(raw=dist_nodes)

    while not Q.is_empty:
        # pick the closest node
        fst = Q.pop().key
        for e in graph.get_neighbourhood(fst):
            # scan the neighbourhood
            snd = e.snd
            weight = e.weight
            if dist[snd] > dist[fst] + weight:
                # update if better route found
                dist[snd] = dist[fst] + weight
                prev[snd] = fst
                Q.bottom_bound_flatten_priority(snd, dist[snd])

    return DijkstraAlgorithmResult(dist=dist, prev=prev)


if __name__ == "__main__":

    graph = read_graph_definition()

    # read starting node
    starting_node = input()
    try:
        starting_node = int(starting_node)
    except ValueError:
        exit('starting node needs to be an integer')

    # measure time
    begin = time()

    # use the Dijkstra's algorithm
    results = Dijkstra_algorithm(graph, starting_node)

    end = time()

    # print out the results
    for node in range(0, graph.nodes_count):

        print(node, results.dist[node])

        # retrace the route back
        route = [
            (
                node,
                graph.get_edge_weight(results.prev[node], node)
            )
        ]
        curr = route[0]
        while curr[0] != starting_node:
            curr = (results.prev[curr[0]], None)
            route.insert(
                0,
                (
                    curr[0],
                    graph.get_edge_weight(results.prev[curr[0]], curr[0])
                )
            )
        # print the route
        print(starting_node, '', file=stderr, end='')
        for r in route[1:]:
            print('-' + str(r[1]) + '→', r[0], '', file=stderr, end='')
        print(file=stderr)

    print((end-begin) * 1000, 'ms', file=stderr)
