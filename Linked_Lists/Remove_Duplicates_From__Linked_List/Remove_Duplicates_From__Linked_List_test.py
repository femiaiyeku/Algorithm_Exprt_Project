"""
Remove Duplicates From Linked List
You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a
function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values.
The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked
List should still have its nodes sorted with respect to their values.
Each Linked List node has an integer value as well as a next node pointing to the next node in the list or
to None/null if it's the tail of the list.

Sample Input:
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

Sample Output:
1 -> 3 -> 4 -> 5 -> 6



"""


from sqlite3 import ProgrammingError
import unittest

class LinkedList:
    def addMany(self, values):
        for value in values:
            self.add(value)
        return self
    
    def getNodesInArray(self):
        nodes = []
        currentNode = self
        while currentNode is not None:
            nodes.append(currentNode.value)
            currentNode = currentNode.next
        return nodes
    
    
class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1)
        test.next = LinkedList(1)
        test.next.next = LinkedList(3)
        test.next.next.next = LinkedList(4)
        test.next.next.next.next = LinkedList(4)
        test.next.next.next.next.next = LinkedList(4)
        test.next.next.next.next.next.next = LinkedList(5)
        test.next.next.next.next.next.next.next = LinkedList(6)
        test.next.next.next.next.next.next.next.next = LinkedList(6)

        expected = LinkedList(1)
        expected.next = LinkedList(3)
        expected.next.next = LinkedList(4)
        expected.next.next.next = LinkedList(5)
        expected.next.next.next.next = LinkedList(6)

        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(ProgrammingError.getNodesInArray(actual), ProgrammingError.getNodesInArray(expected))

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return linkedList

if __name__ == "__main__":
    unittest.main()

    

