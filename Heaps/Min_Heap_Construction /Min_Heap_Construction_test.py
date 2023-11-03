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

from sqlite3 import ProgrammingError
import unittest

def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        minHeap = ProgrammingError.MinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        minHeap.insert(0)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 0)
        self.assertEqual(minHeap.remove(), 0)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 1)
        self.assertEqual(minHeap.remove(), 1)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        minHeap.insert(0)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 0)
        self.assertEqual(minHeap.remove(), 0)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

if __name__ == "__main__":
    unittest.main()

    