#!/usr/bin/env python3


class SimpleGraph(object):
    def __init__(self):
        self.vertex_nbh = {}

    @property
    def vertices(self):
        """Returns graph's verticies.
        """
        return list(self.vertex_nbh.keys())

    @property
    def edges(self):
        """Returns graph's edges.
        """
        edges = []
        for x in self.vertex_nbh:
            for y in self.vertex_nbh[x]:
                if {y, x} not in edges:
                    edges.append({x, y})
        return edges

    def add_vertex(self, x):
        """Adds vertex to the graph.

        If vertex `x` is not in `self.vertex_nbh` then `x` is added with
        an empty list of neighbours is added.
        Otherwise no action is performed.
        """
        if x not in self.vertex_nbh:
            self.vertex_nbh[x] = []

    def _add_edge(self, x, y):
        """Internal one-way edge adder.
        """
        if x in self.vertex_nbh:
            if y not in self.vertex_nbh[x]:
                self.vertex_nbh[x].append(y)
        else:
            self.vertex_nbh[x] = [y]

    def add_edge(self, x, y):
        """Adds an edge between two verticies.
        """
        self._add_edge(x, y)
        self._add_edge(y, x)

    def neighbours(self, v):
        return self.vertex_nbh[v]

    def deg(self, v):
        return len(self.vertex_nbh.get(v))

    def _degs(self):
        """Utility internal function for *_deg methods."""
        return map(lambda x: self.deg(x), self.vertices)

    def min_deg(self):
        """Returns minimal degree of any vertex in graph."""
        return min(self._degs())

    def max_deg(self):
        """Returns maximal degree of any vertex in graph."""
        return max(self._degs())

    def avg_deg(self):
        """Returns average degree of verticies in graph."""
        return sum(self._degs())/len(self.vertex_nbh)

    def ecc(self, v):
        output = 0
        visited = [v]
        active = self.neighbours(v)
        while active != []:
            output += 1
            visited += active
            active = [y for x in active for y in self.neighbours(
                x) if y not in visited]

        if set(visited) != set(self.vertices):
            return float('inf')

        return output

    @property
    def radius(self):
        return min(
            map(lambda v: self.ecc(v), self.vertices)
        )

    @property
    def diameter(self):
        return max(
            map(lambda v: self.ecc(v), self.vertices)
        )

    @property
    def spanning_tree(self):
        """Builds a spanning tree of the original tree.
        """
        if self.ecc(self.vertices[0]) == float('inf'):
            raise Exception('disconnected graph, can\'t build a spanning tree')

        spanning = SimpleGraph()
        # copy the vertices over
        for v in self.vertices:
            spanning.add_vertex(v)

        root = self.vertices[0]

        # previously active that are the target to connect for the currently active
        active_prev = [root]
        # visited nodes
        visited = [root]
        # currently processed nodes
        active = self.neighbours(root)
        while set(visited) != set(self.vertices):
            for v in active:
                # for every non-connected node in the spanning graph...
                if spanning.deg(v) == 0:
                    # ...find a node from the previously active to connect
                    for possible in active_prev:
                        if set([v, possible]) in self.edges:
                            # found that is actually connected in the original graph
                            spanning.add_edge(v, possible)
                            break
            visited += active
            active_prev = active
            active = [y for x in active for y in self.neighbours(
                x) if y not in visited]

        return spanning


if __name__ == '__main__':
    graph = SimpleGraph()

    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    graph.add_edge('a', 'd')
    graph.add_edge('b', 'a')
    graph.add_edge('c', 'b')
    graph.add_edge('c', 'd')
    graph.add_edge('d', 'a')
    graph.add_edge('d', 'c')
    graph.add_edge('d', 'e')

    # graph.add_edge('f', 'g')

    print('Vertices of graph:')
    print(graph.vertices)
    print('min deg =', graph.min_deg())
    print('max deg =', graph.max_deg())
    print('avg deg =', graph.avg_deg())
    print()
    print('eccentricity of every vertex:')
    for v in graph.vertices:
        print('ecc(' + v + ') =', graph.ecc(v))
    print()
    print('radius =', graph.radius)
    print('diameter =', graph.diameter)

    print()

    print('Edges of graph:')
    print(graph.edges)

    print()

    print('Spanning tree edges:')
    print(graph.spanning_tree.edges)
