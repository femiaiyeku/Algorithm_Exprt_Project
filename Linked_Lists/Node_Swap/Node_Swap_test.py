"""

Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e.,
doesn't create a brand new list), and returns its new head.
If the input Linked List has an odd number of nodes, its final node should remain the same.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or
to None/null if it's the tail of the list.
You can assume that the input Linked List will always have at least one node; in other words, the head will never
be None / null.

Sample Input

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0


Sample Output

1 -> 0 -> 3 -> 2 -> 5 -> 4 // the head node with value 1

"""


from sqlite3 import ProgrammingError
import unittest

class LinkedList(ProgrammingError.LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
            for value in values:
                current.next = LinkedList(value)
                current = current.next
                for value in values:
                    current.next = LinkedList(value)
                    current = current.next
                    return self


def getNodesInArray(head):
    nodes = []
    while head is not None:
        nodes.append(head.value)
        head = head.next
        return nodes
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        result =ProgrammingError.nodeSwap(test)
        self.assertEqual(getNodesInArray(result), [1, 0, 3, 2, 5, 4])


if __name__ == "__main__":
    unittest.main()






