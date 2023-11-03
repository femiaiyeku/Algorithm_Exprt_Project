"""
You're given a list of edges representing a weighted, undirected graph with at least one node. 
The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to the length of edges , 
where each index i in edges contains vertex i ·s siblings, in no particular order. 
Each of these siblings is an array of length two, with the first value denoting the index in the list that this vertex is connected to,
 and and the second value denoting the weight of the edge. Note that this graph is undirected, 
meaning that if a vertex appears in the edge list of another vertex, then the inverse will also be true (along with the same weight). 
Write a function implementing Kruskal's Algorithm to return a new edges array that represents a minimum spanning tree. 
A minimum spanning tree is a tree containing all of the vertices of the original graph and a subset of the edges. 
These edges should connect all of the vertices with the minimum total edge weight and without generating any cycles. 
If the graph is not connected, your function should return the minimum spanning forest {i.e. all of the nodes should be able to reach the same nodes as they could in the initial edge list). 
Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves) and will only have positively weighted edges {i.e., no negative distances). 
If you're unfamiliar with Kruskal's algorithm, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 
If you're unfamiliar with the Union Find data structure, we recommend completing that problem before attempting this one. 


Sample Input:
edges = [
    [1, 2, 3],
    [1, 3, 4],
    [4, 5, 8],
    [1, 5, 9],
    [2, 5, 10],
    [3, 4, 2],
    [3, 5, 6],
    [2, 4, 7],
]


Sample Output:
[
    [1, 2, 3],
    [3, 4, 2],
    [1, 3, 4],
    [4, 5, 8],
]

// The output can be any ordering of the subarrays as long as they all follow format of [vertexOne, vertexTwo, weight] and are all included in edges or are an inverse of an included subarray.

"""

from dataclasses import dataclass, field

dataclass(order=True)

class Edge:
    outgoing: int = field(compare=False)
    incoming : int = field(compare=False)
    weight: int = field(compare=True)

    #O(Elog(E)) time | O(E) space

    def refine_edges(edges):
        refined_edges = []
        for outgoing_vertex, destination in enumerate(edges):
            for incoming_vertex, weight in destination:
                if incoming_vertex > outgoing_vertex:
                    refined_edges.append(Edge(outgoing_vertex, incoming_vertex, weight))

        return refined_edges
    
    def kruskals_algorithm(edges):
        refined_edges = Edge.refine_edges(edges)
        refined_edges.sort()
        union_find = UnionFind(len(edges))
        minimum_spanning_tree = []

        for edge in refined_edges:
            if union_find.are_connected(edge.outgoing, edge.incoming):
                continue
            union_find.connect(edge.outgoing, edge.incoming)
            minimum_spanning_tree.append([edge.outgoing, edge.incoming, edge.weight])

        return minimum_spanning_tree
    

class UnionFind:
    def __init__(self, length):
        self.parent = list(range(length))
        self.rank = [1] * length

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    
    def are_connected(self, x, y):
        return self.find(x) == self.find(y)

    def connect(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False

        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1


        return True
    



