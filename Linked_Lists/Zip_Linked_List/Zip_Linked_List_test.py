"""

You're given the head of a Singly Linked List of arbitrary length k .
 Write a function that zips the Linked List in place (i.e., doesn't create a brand new list) and returns its head. 
A Linked List is zipped if its nodes are in the following order, where k 1s the length of the Linked List: 

1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...


Each Linked List node has an integer value as well as a next node pointing to the next node in the 11st or to None I null 1f it's the tail of the list. 
You can assume that the input Linked List will always have at least one node; in other words, the head will never be None I null 

Sample Input:
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

Sample Output:
0 -> 5 -> 1 -> 4 -> 2 -> 3 // the head node with value 0


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
    
    def __eq__(self, other):
        return self.getNodesInArray() == other.getNodesInArray()
    
def zipLinkedList(head):
    if head.next is None:
        return head
    
    firstHalfHead = head
    secondHalfHead = splitLinkedList(head)
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)
    return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)


def splitLinkedList(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    secondHalfHead = slow.next
    slow.next = None
    return secondHalfHead

def reverseLinkedList(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    
    return previous

def interweaveLinkedLists(list1, list2):
    list1Pointer = list1
    list2Pointer = list2
    while list1Pointer is not None and list2Pointer is not None:
        list1PointerNext = list1Pointer.next
        list2PointerNext = list2Pointer.next

        list1Pointer.next = list2Pointer
        list2Pointer.next = list1PointerNext

        list1Pointer = list1PointerNext
        list2Pointer = list2PointerNext
    
    return list1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        inputLinkedList = LinkedList(0).addMany([1, 2, 3, 4, 5])
        outputLinkedList = LinkedList(0).addMany([5, 1, 4, 2, 3])
        self.assertTrue(ProgrammingError.zipLinkedList(inputLinkedList) == outputLinkedList)

if __name__ == "__main__":
    unittest.main()

    