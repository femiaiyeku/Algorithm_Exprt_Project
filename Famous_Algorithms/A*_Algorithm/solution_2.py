"""
You're given a two-dimensional array containing 0 sand 1 s, where each 0 represents a free space and each 1 represents an obstacle (a space that cannot be passed through). You can think of this array as a grid-shaped graph. You're also given four integers startRow, startCol , endRow, and endCol , representing the positions of a start node and an end node in the graph. 
Write a function that finds the shortest path between the start node and the end node using the A* search algorithm and returns it. 
The shortest path should be returned as an array of node positions, where each node position is an array of two elements: the 
[row, col] of the respective node in the graph. The output array should contain the start node's position, the end node's position, and all of the positions of the remaining nodes in the shortest path, and these node positions should be ordered from start node to end node. 
If there is no path from the start node to the end node, your function should return an empty array. 
Note that: 

• 	From each node in the graph, you can only travel in four directions: up, left, down and right; you can't travel diagonally. 
• 	The distance between all neighboring nodes in the graph is the same; you can treat it as a distance of 1. 
• 	The start node and end node are guaranteed to be located in empty spaces (cells containing e ). 
• 	The start node and end node will never be out of bounds and will never overlap. 
• 	There will be at most one shortest path from the start node to the end node. 

If you're unfamiliar with A*, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 

Sample Input:

grid = [
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

startRow = 0
startCol = 0
endRow = 5
endCol = 5

Sample Output:

[[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [3, 4], [3, 5], [4, 5], [5, 5]]

// The shortest path is highlighted below:


[  
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 2],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [4, 5],
    [5, 5]
]

    
"""


import heapq
def aStartAlgorithm(startRow, startCol, endRow, endCol, graph):
    S = (startRow, startCol)
    E = (endRow, endCol)
    OL, H, CL, D, P, C = {S:0}, [(0, S)], set(), {(startRow, startCol):0}, {}, 0
    while H:
        C += 1
        d, node = heapq.heappop(H)
        CL.add(node)
        if node == E:
            return P
        for n in getNeighbours(node, graph):
            if n in CL:
                continue
            if n not in OL or OL[n] > D[node] + 1:
                D[n] = D[node] + 1
                P[n] = node
                OL[n] = D[n] + getManhattanDistance(n, E)
                heapq.heappush(H, (OL[n], n))

def getNeighbours(node, graph):
    r, c = node
    neighbours = []
    if r > 0 and graph[r-1][c] == 0:
        neighbours.append((r-1, c))
    if r < len(graph) - 1 and graph[r+1][c] == 0:
        neighbours.append((r+1, c))
    if c > 0 and graph[r][c-1] == 0:
        neighbours.append((r, c-1))
    if c < len(graph[0]) - 1 and graph[r][c+1] == 0:
        neighbours.append((r, c+1))
    return neighbours



def getManhattanDistance(node, end):
    r1, c1 = node
    r2, c2 = end
    return abs(r1 - r2) + abs(c1 - c2)

graph = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

startRow = 0
startCol = 0
endRow = 5
endCol = 5

print(aStartAlgorithm(startRow, startCol, endRow, endCol, graph))


