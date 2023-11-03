"""
Implement a MinHeap class that supports:


• 	Building a Min Heap from ar input array of integers. 
• 	Inserting integers in the heaJ. 
• 	Removing the heap's minimum/ root value. 
• 	Peeking at the heap's minimum/ root value. 
• 	Sifting integers up and dowr, the heap, which is to be used when inserting and removing values.

Note that the heap should be repr􀀌sented in the form of an array. 
If you're unfamiliar with Min Heaps, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 

Sample Usage

// All operations below are performed sequentially.

MinHeap(array)
// - buildHeap(array):
//   - takes in an array of integers and builds a min heap from them.
//   - returns the input array modified in place.
buildHeap([9, 4, 7, 1, -2, 6, 5])
//   -> [-2, 1, 5, 9, 4, 6, 7]
// - insert(8):
//   - inserts the value 8 into the heap.
insert(8)
// - remove():
//   - removes the minimum value (that is, the root value) from the heap.
remove()
//   -> -2
// - peek():
//   - returns the minimum value from the heap without removing it.
peek()
//   -> 1
// - insert(-3):
//   - inserts the value -3 into the heap.
insert(-3)
//   -> [-3, 1, 5, 9, 4, 6, 7, 8]

Hints & Tips
• 	The heapify procedure is a common procedure used in heaps.
• 	You can use the siftDown procedure to implement the remove procedure.
• 	You can use the siftUp procedure to implement the insert procedure.
• 	You can use the siftDown procedure to implement the buildHeap procedure.
• 	You can use the siftUp procedure to implement the insert procedure.


"""


import heapq
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
        heapq.heapify(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
            

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if heap[currentIdx] < heap[parentIdx]:
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return
            
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        heapq.heapify(self.heap)
        return valueToRemove
    
    def insert(self, value):
        self.heap.append(value)
        heapq.heapify(self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


        