"""
Write a ContinuousMedianHandler class that supports:
• 	The continuous insertion of numbers with the insert method. 
• 	The instant (0(1) time) retrieval of the median of the numbers that have been inserted thus far with the getMedi an method. 

The getMedian method has already been written for you. You simply have to write the insert method. 
The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest.
 If there's an odd number of numbers in the set, as in {l, 3, 7} , the median is the number in the middle ( 3 in this case); if there's an even number of numbers in the set, as in {l, 3, 7, 8} , the median is the average of the two middle numbers { 
(3 + 7) / 2 == 5 in this case) 

Sample Input:
insert(5)
insert(10)
getMedian()
insert(100)
getMedian()

Sample Output:
5
7.5

"""

import heapq
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.lower = []
        self.upper = []
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)

    def insert(self, number):
        if not self.lower or number < -self.lower[0]:
            heapq.heappush(self.lower, -number)
        else:
            heapq.heappush(self.upper, number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if len(self.lower) - len(self.upper) == 2:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) - len(self.lower) == 2:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def updateMedian(self):
        if len(self.lower) == len(self.upper):
            self.median = (-self.lower[0] + self.upper[0]) / 2
        elif len(self.lower) > len(self.upper):
            self.median = -self.lower[0]
        else:
            self.median = self.upper[0]


    def getMedian(self):
        return self.median
    
class Heap:
    def __init__(self, comparisonFunc, array):
        self.heap = self.buildHeap(array)
        self.comparisonFunc = comparisonFunc
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


if __name__ == "__main__":
    pass






  