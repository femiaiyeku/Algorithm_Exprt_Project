"""

Prim's Algorithm
You're given a list of edges representing a connected, weighted, undirected graph with at least one node.
The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to
the length of edges, where each index in edges contains vertex's siblings, in no particular order. Each of
these siblings is an array of length two, with the first value denoting the index in the list that this vertex is connected to,
and and the second value denoting the weight of the edge. Note that this graph is undirected, meaning that if a vertex
appears in the edge list of another vertex, then the inverse will also be true (along with the same weight).
Write a function implementing Prim's Algorithm to return a new edges array that represents a minimum spanning
tree. A minimum spanning tree is a tree containing all of the vertices of the original graph and a subset of the edges.
These edges should connect all of the vertices with the minimum total edge weight and without generating any cycles.
Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to
themselves) and will only have positively weighted edges (l.e., no negative distances). The graph will always have at least
one node.
If you're unfamiliar with Prim's algorithm, we recommend watching the Conceptual Overview section of this question's
video explanation before starting to code.


Sample Input:
edges = [
    [[1, 7]],
    [[2, 8], [3, 3], [4, 6]],
    [[3, 4]],
    [[4, 2]],
    [],
    []
]

Sample Output:
[
    [[1, 7]],
    [[0, 7], [3, 3], [4, 6]],
    [[3, 4]],
    [[1, 3]],
    [[1, 6]],
    []
]

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 7], [2, 8], [3, 3], [4, 6], [], []]
        expected = [[], [0, 7], [3, 3], [0, 7], [0, 7], []]
        actual = ProgrammingError.primsAlgorithm(input)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

    


