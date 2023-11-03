"""
You're given a list of edges representing a connected, unweighted, undirected graph with at least one node. Write a
function that returns a boolean representing whether the given graph is two-colorable.
A graph is two-colorable (also called bipartite) if all of the nodes can be assigned one of two colors such that no nodes
of the same color are connected by an edge.
The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to
the length of edges, where each index i in edges contains vertex's siblings, in no particular order. Each
individual edge is represented by a positive integer that denotes an index in the list that this vertex is connected to.
Note that this graph is undirected, meaning that if a vertex appears in the edge list of another vertex, then the inverse
will also be true.
Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; in
other words, it's an edge that connects a vertex to itself. Any self-loop should make a graph not 2-colorable.

Sample Input:

edges = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

Sample Output:

true

// The following graph is two-colorable:
// 0: R
// 1: B
// 2: R
// 3: B
// Every vertex can have a color that is different than the color of its immediate neighbors.

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        edges = [
            [1, 3],
            [0, 2],
            [1, 3],
            [0, 2]
        ]
        self.assertTrue(ProgrammingError.twoColorable(edges))

    def test_case_2(self):
        edges = [
            [1, 2, 3],
            [0, 2],
            [1, 3],
            [0, 2]
        ]
        self.assertFalse(ProgrammingError.twoColorable(edges))


if __name__ == '__main__':
    unittest.main()

    


