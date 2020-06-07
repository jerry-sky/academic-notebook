from graph import Graph
from decimal import Decimal


def read_graph_definition() -> Graph:
    """Reads a graph definition from `stdin`.
    """

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

    return graph
