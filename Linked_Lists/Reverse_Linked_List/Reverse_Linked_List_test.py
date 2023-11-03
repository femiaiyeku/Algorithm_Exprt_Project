"""
Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a brand
new list), and returns its new head.
Each LinkedList node has an integer value as well as a next] node pointing to the next node in the list or
to None / null if it's the tail of the list.
You can assume that the input Linked List will always have at least one node; in other words, the head will never
be None / null.

Sample Input:

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

Sample Output:

5 -> 4 -> 3 -> 2 -> 1 -> 0 // the new head node with value 5



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
                
                def getNodesInArray(self):
                    nodes = []
                    current = self
                    while current is not None:
                        nodes.append(current.value)
                        current = current.next
                        return nodes
                    
                    def compare(self, nodes):
                        current = self
                        for value in nodes:
                            if current.value != value:
                                return False
                            current = current.next
                            return current is None
                        
                        def reverseLinkedList(head):
                            previousNode, currentNode = None, head
                            while currentNode is not None:
                                nextNode = currentNode.next
                                currentNode.next = previousNode
                                previousNode = currentNode
                                currentNode = nextNode
                                return previousNode
                            
                            class TestProgram(unittest.TestCase):
                                def test_case_1(self):
                                    test = ProgrammingError.LinkedList(0)
                                    test.addMany([1, 2, 3, 4, 5])
                                    self.assertTrue(test.compare([0, 1, 2, 3, 4, 5]))
                                    rev = reverseLinkedList(test)
                                    self.assertTrue(rev.compare([5, 4, 3, 2, 1, 0]))
                                    
                                    def main():
                                        unittest.main()
                                        
                                        if __name__ == "__main__":
                                            main()


                


