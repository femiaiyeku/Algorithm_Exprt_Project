"""
You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative integer,
where each node in the Linked List is a digit of that integer, and the first node in each Linked List always
represents the least significant digit of the integer. Write a function that returns the head of a new Linked List that
represents the sum of the integers represented by the two input Linked Lists.
Each LinkedList node has an integer value as well as a next node pointing to the next nade in the list or
None / null if it's the tail of the list. The value of each LinkedList node is always in the range of
Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input
Linked Lists.

Sample Input:
LinkedListOne = 2 -> 4 -> 7 -> 1
LinkedListTwo = 9 -> 4 -> 5

Sample Output:
1 -> 9 -> 2 -> 2
// Linked List representation of 1742 + 549 = 2291


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
        return self
    
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedListOne = LinkedList(2).addMany([4, 7, 1])
        linkedListTwo = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = ProgrammingError.sumOfLinkedLists(linkedListOne, linkedListTwo)
        self.assertEqual(expected.getNodesInArray(), actual.getNodesInArray())



                
