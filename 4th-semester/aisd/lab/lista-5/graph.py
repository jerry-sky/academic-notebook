from collections import namedtuple
from typing import Iterable

GraphEdge = namedtuple('GraphEdge', ['fst', 'snd', 'weight'])


class Graph(object):
    """Implements such a graph that the nodes are represented
    by consecutive natural numbers starting at `0`.
    """

    def __init__(self, nodes_count: int):
        self.__edges = []
        self.__nodes_count = nodes_count

    @property
    def edges(self):
        return self.__edges

    @property
    def nodes_count(self):
        return self.__nodes_count

    def add_edge(self, fst: int, snd: int, weight: float = 1., twoway: bool = False):
        """Adds a new edge to the graph between `fst` and `snd` of weight `weight`.
        There is an option to make the new edge twoway (`twoway=True`).
        """
        # assert - nodes' labels has to be between `1` and `nodes_count`
        if fst >= self.__nodes_count or snd >= self.__nodes_count:
            raise Exception(
                'node label exceed maximum number of nodes in graph')

        # add a new edge
        self.__edges.append(
            GraphEdge(fst=fst, snd=snd, weight=weight)
        )
        if twoway:
            self.__edges.append(
                GraphEdge(fst=snd, snd=fst, weight=weight)
            )

    def get_neighbourhood(self, source: int) -> Iterable[GraphEdge]:
        """Returns all edges that start at the given source node.
        """
        return filter(
            lambda e: e.fst == source,
            self.__edges
        )

    def get_edge_weight(self, fst: int, snd: int) -> float:
        """Return the weight of the given edge.
        """
        try:
            return next(
                filter(
                    lambda e: e.fst == fst and e.snd == snd,
                    self.__edges
                )
            ).weight
        except StopIteration:
            return None
