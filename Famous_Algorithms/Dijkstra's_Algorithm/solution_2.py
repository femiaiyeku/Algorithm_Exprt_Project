"""
You're given an integer start and a list edges of pairs of integers. 
The list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to the length of edges , where each index i in edges contains vertex i 's outbound edges, in no particular order. Each individual edge is represented by an pair of two numbers, [des ti nation, di stance] , where the destination is a positive integer denoting the destination vertex and the distance is a positive integer representing the length of the edge (the distance from vertex i to vertex des ti nation ). Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination-not the other way around (unless the destination vertex itself has an outbound edge to the original vertex). 
Write a function that computes the lengths of the shortest paths between start and all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array. 
Each index i in the output array should represent the length of the shortest path between start and vertex i . If no path is found from start to vertex i , 
then output [i] should be -1 
Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves) 
and will only have positively weighted edges (i.e., no negative distances). 
If you're unfamiliar with Dijkstra's algorithm, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 


Sample Input
start = 0
edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
]

Sample Output
[0, 7, 13, 27, 10, -1]



"""

from heapq import heappush, heappop

def dijkstrasAlgorithm(start, edges):
    total_vertices = len(edges)

    graph = {i : edges[i] for i in range(total_vertices)}


    min_heap = [ (0, start) ]
    visited = set()

    output = [-1 for _ in range(total_vertices)]

    while min_heap:
        dist, node = heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        output[node] = dist

        for neighbor, neighbor_dist in graph[node]:
            if neighbor not in visited:
                heappush(min_heap, (dist + neighbor_dist, neighbor))

    return output


if __name__ == "__main__":
    start = 0
    edges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        [],
    ]

    print(dijkstrasAlgorithm(start, edges))

    