#!/usr/bin/env python3
from typing import Iterable
from graph import Graph, GraphEdge, INFINITY
from graph_input_utility import read_graph_definition
from priority_queue import PriorityQueue, PQNode
from sys import exit, argv


def Kruskal(graph: Graph) -> Iterable[GraphEdge]:
    """Returns a MST using Kruskal's algorithm.
    """

    # create disjoint sets for all nodes in the graph
    disjoint_sets = [i for i in range(0, graph.nodes_count)]

    def find(a):
        node = a
        while node != disjoint_sets[node]:
            node = disjoint_sets[node]
        return node

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        disjoint_sets[root_b] = root_a

    mst = []

    # sort the edges
    edges = sorted(graph.edges, key=lambda x: x.weight)

    for e in edges:
        fst, snd = e.fst, e.snd
        if find(fst) != find(snd):
            mst.append(e)
            union(fst, snd)

    return mst


def Prim(graph: Graph) -> Iterable[GraphEdge]:
    """Returns a MST using Prim's algorithm.
    """

    cost = [INFINITY for _ in range(graph.nodes_count)]
    prev = [None for _ in range(graph.nodes_count)]

    # take the first node as the starting node
    starting_node = 0

    cost[starting_node] = 0
    prev[starting_node] = starting_node

    # build a priority queue
    cost_nodes = [
        PQNode(key=i, priority=cost[i])
        for i in range(0, graph.nodes_count)
    ]
    Q = PriorityQueue(raw=cost_nodes)

    while not Q.is_empty:
        fst = Q.pop().key
        for e in graph.get_neighbourhood(fst):
            snd = e.snd
            weight = graph.get_edge_weight(fst, snd, twoway=True)
            if cost[snd] > weight:
                cost[snd] = weight
                prev[snd] = fst
                Q.bottom_bound_flatten_priority(snd, cost[snd])

    # render out actual graph edges using the `prev` list
    mst = []
    for node in range(0, graph.nodes_count):
        if node == starting_node:
            continue
        mst.append(
            GraphEdge(prev[node], node, graph.get_edge_weight(
                prev[node], node, twoway=True))
        )

    return mst


if __name__ == "__main__":

    if len(argv) < 2:
        exit('usage: ./msts.py <-p|-k>')

    alg = argv[1]

    graph = read_graph_definition()

    spanning_tree_edges = Kruskal(graph) if alg == '-k' else Prim(graph)

    # print all spanning tree edges
    for e in spanning_tree_edges:
        fst, snd = sorted([e.fst, e.snd])
        weight = e.weight
        print(fst, snd, weight)
    # print the total cost of the spanning tree
    print(sum(map(lambda x: x.weight, spanning_tree_edges)))
