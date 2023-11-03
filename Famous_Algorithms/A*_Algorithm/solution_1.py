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


class Node:
    def __init__(self, row, col, distance, estimated_distance):
        self.row = row
        self.col = col
        self.value = ValueError
        self.distanceFromStart = float("inf")
        self.estimatedDistanceToEnd = float("inf")
        self.cameFrom = None


# O(w*h*log(w*h)) time | O(w*h) space - where w and h are the width and height of the input grid
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]
    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)

    nodesToVisit = MinHeap([startNode])

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()
        if currentMinDistanceNode == endNode:
            break

        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue

            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1
            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue

            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = (
                tentativeDistanceToNeighbor + calculateManhattanDistance(neighbor, endNode)
            )

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)

    return reconstructPath(endNode)


def initializeNodes(graph):
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes


def calculateManhattanDistance(currentNode, endNode):
    currentRow, currentCol = currentNode.row, currentNode.col
    endRow, endCol = endNode.row, endNode.col
    return abs(currentRow - endRow) + abs(currentCol - endCol)


def getNeighboringNodes(node, nodes):
    neighbors = []
    numRows = len(nodes)
    numCols = len(nodes[0])
    row = node.row
    col = node.col

    if row < numRows - 1:
        neighbors.append(nodes[row + 1][col])
    if row > 0:
        neighbors.append(nodes[row - 1][col])
    if col < numCols - 1:
        neighbors.append(nodes[row][col + 1])
    if col > 0:
        neighbors.append(nodes[row][col - 1])

    return neighbors


def reconstructPath(endNode):
    if endNode.cameFrom is None:
        return []
    currentNode = endNode
    path = []
    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom
    return path[::-1]


class MinHeap:

    def __init__(self, array):
        self.nodePositionsInHeap = {node: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if (
                childTwoIdx != -1
                and heap[childTwoIdx].estimatedDistanceToEnd
                < heap[childOneIdx].estimatedDistanceToEnd
            ):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1


def insert(self, node):
    self.heap.append(node)
    self.nodePositionsInHeap[node] = len(self.heap) - 1
    self.siftUp(len(self.heap) - 1, self.heap)


def remove(self):
    if self.isEmpty():
        return
    self.swap(0, len(self.heap) - 1, self.heap)
    node = self.heap.pop()
    del self.nodePositionsInHeap[node]
    self.siftDown(0, len(self.heap) - 1, self.heap)
    return node


def containsNode(self, node):
    return node in self.nodePositionsInHeap


def update(self, node):
    self.siftUp(self.nodePositionsInHeap[node], self.heap)


def swap(self, i, j, heap):
    self.nodePositionsInHeap[heap[i]], self.nodePositionsInHeap[heap[j]] = (
        self.nodePositionsInHeap[heap[j]],
        self.nodePositionsInHeap[heap[i]],
    )
    heap[i], heap[j] = heap[j], heap[i]


def siftUp(self, currentIdx, heap):
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
        self.swap(currentIdx, parentIdx, heap)
        currentIdx = parentIdx
        parentIdx = (currentIdx - 1) // 2


def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if (
            childTwoIdx != -1
            and heap[childTwoIdx].estimatedDistanceToEnd
            < heap[childOneIdx].estimatedDistanceToEnd
        ):
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
            self.swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return
        

