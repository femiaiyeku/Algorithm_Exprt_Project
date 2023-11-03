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

#O(v^2 + e) time | O(v) space - where v is the number of vertices of the input graph and e is the number of edges of the input graph

def primsAlgorithm(edges):
    minHeap = MinHeap([(0, i) for i in range(len(edges))])
    minHeap.updatePriority(0, 0)
    visited = set()
    mstEdges = [None for _ in edges]
    while not minHeap.isEmpty():
        _, vertex = minHeap.remove()
        if vertex in visited:
            continue
        visited.add(vertex)
        for edge in edges[vertex]:
            destination, distanceToDestination = edge
            if destination in visited:
                continue
            if distanceToDestination < minHeap.heap[destination][0]:
                minHeap.updatePriority(destination, distanceToDestination)
                mstEdges[destination] = [vertex, destination]

    return getMinSpanningTree(edges, mstEdges)

def getMinSpanningTree(edges, mstEdges):
    minSpanningTree = []
    for edge in mstEdges:
        if edge is None:
            minSpanningTree.append([])
            continue
        minSpanningTree.append([edge[0], edge[1]])
    return minSpanningTree

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    def siftDown(self, currentIdx, endIdx, heap):
        def siftDown(self, currentIdx, endIdx, heap):
            childOneIdx = currentIdx * 2 + 1
            while childOneIdx <= endIdx:
                childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
                if childTwoIdx != -1 and heap[childTwoIdx][0] < heap[childOneIdx][0]:
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
                if heap[idxToSwap][0] < heap[currentIdx][0]:
                    self.swap(currentIdx, idxToSwap, heap)
                    currentIdx = idxToSwap
                else:
                    break
                childOneIdx = currentIdx * 2 + 1

        def siftUp(self, currentIdx, heap):
            parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][0] < heap[parentIdx][0]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def updatePriority(self, idx, value):
        self.heap[idx] = (value, self.heap[idx][1])
        self.siftUp(idx, self.heap)

# if __name__ == '__main__':
#     edges = [
#         [[1, 7]],
#         [[2, 8], [3, 3], [4, 6]],
#         [[3, 4]],
#         [[4, 2]],
#         [],
#         []
#     ]

#     print(primsAlgorithm(edges))



