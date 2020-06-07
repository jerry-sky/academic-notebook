#!/usr/bin/env python3
from collections import namedtuple
from graph import Graph
from priority_queue import PriorityQueue, PQNode
from sys import exit, stdin, stderr
from time import time
from decimal import Decimal

INFINITY = float('inf')

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

    nodes_count = input()
    try:
        nodes_count = int(nodes_count)
    except ValueError:
        exit('nodes count needs to be an integer')

    edges_count = input()
    try:
        edges_count = int(edges_count)
    except ValueError:
        exit('edges count needs to be an integer')

    # create a new graph
    graph = Graph(nodes_count)

    # read edges
    for _ in range(edges_count):
        raw_edge = input().split()

        fst, snd, weight = 0, 0, 0
        try:
            fst, snd, weight = int(raw_edge[0]), int(
                raw_edge[1]), Decimal(raw_edge[2])
        except (ValueError, IndexError):
            exit('edge definition format: int int float')

        graph.add_edge(fst=fst, snd=snd, weight=weight)

    # read starting node
    starting_node = input()
    try:
        starting_node = int(starting_node)
    except ValueError:
        exit('starting node needs to be an integer')

    # use the Dijkstra algorithm
    results = Dijkstra_algorithm(graph, starting_node)

    # print out the results
    for node in range(0, nodes_count):

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
