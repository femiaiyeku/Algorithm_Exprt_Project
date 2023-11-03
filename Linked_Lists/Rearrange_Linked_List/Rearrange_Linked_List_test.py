"""
Write a function that takes in the head of a Singly Linked List and an integer k , rearranges the list in place (i.e., doesn·t create a brand new list) around nodes with value k , and returns its new head. 
Rearranging a Linked List around nodes with value k means moving all nodes with a value smaller than k before all nodes with value k and moving all nodes with a value greater than k after all nodes with value k 
All moved nodes should maintain their original relative ordering if possible. 
Note that the linked list should be rearranged even 1f 1t doesn·t have any nodes with value k 
Each Linked list node has an integer value as well as a next node pointing to the next node in the list or to None / null 1f it's the tad of the list. 
You can assume that the input Linked List will always have at least one node; 1n other words, the head will never be None / null. 

Sample Input:
head = 3 -> 0 -> 5 -> 2 -> 1 -> 4 // the head node with value 3
k = 3
Sample Output:
0 -> 2 -> 1 -> 3 -> 5 -> 4 // the new head node with value 0

"""


from sqlite3 import ProgrammingError
import unittest

def linkedListToArray(head):
    array = []
    node = head
    while node is not None:
        array.append(node.value)
        node = node.next
    return array

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = ProgrammingError.LinkedList(3)
        head.next = ProgrammingError.LinkedList(0)
        head.next.next = ProgrammingError.LinkedList(5)
        head.next.next.next = ProgrammingError.LinkedList(2)
        head.next.next.next.next =ProgrammingError.LinkedList(1)
        head.next.next.next.next.next = ProgrammingError.LinkedList(4)
        k = 3
        expected = [0, 2, 1, 3, 5, 4]
        actual = linkedListToArray(rearrangeLinkedList(head, k))
        self.assertEqual(actual, expected)

def growLinkedList(head, tail, node):
    newHead = head
    newTail = node
    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node
    return (newHead, newTail)

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo
    if tailOne is not None:
        tailOne.next = headTwo
    return (newHead, newTail)

def rearrangeLinkedList(head, k):
    # Write your code here.
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None
    node = head
    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail, node)
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
        else:
            equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)
        prevNode = node
        node = node.next
        prevNode.next = None
    firstHead, firstTail = connectLinkedLists(smallerListHead, smallerListTail, equalListHead, equalListTail)
    finalHead, _ = connectLinkedLists(firstHead, firstTail, greaterListHead, greaterListTail)
    return finalHead
