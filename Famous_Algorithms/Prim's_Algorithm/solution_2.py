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

import heapq


def primsAlgorithm(edges):
    
    # Initialize the min spanning tree edges array

    # Initialize the min heap

    # Initialize the visited set

    # While the min heap is not empty

        # Remove the vertex with the smallest key from the min heap

        # If that vertex has already been visited, continue

        # Add that vertex to the visited set

        # For each edge in the current vertex's edges

            # Get the destination vertex and the distance to that destination vertex

            # If the destination vertex has already been visited, continue

            # If the distance to the destination vertex is less than the current key in the min heap

                # Update the key in the min heap

                # Update the edge in the min spanning tree edges array

    # Return the min spanning tree edges array

    minSpanningTree = [[]for _ in edges]
    nodesVisited = set([0])
    minHeap = [(weight, 0, destination) for destination, weight in edges[0]]
    heapq.heapify(minHeap)

    while len(nodesVisited) < len(edges):
        weight, source, destination = heapq.heappop(minHeap)
        if destination in nodesVisited:
            continue
        nodesVisited.add(destination)
        minSpanningTree[source].append([source, destination])
        for neighbor, weight in edges[destination]:
            if neighbor not in nodesVisited:
                heapq.heappush(minHeap, (weight, destination, neighbor))
    return minSpanningTree




#O(v + e) time | O(v + e) space - where v is the number of vertices of the input graph and e is the number of edges of the input graph

