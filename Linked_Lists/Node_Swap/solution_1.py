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

# O(n) time | O(1) space - where n is the number of nodes in the Linked List

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def nodeSwap(head):
    if head is None or head.next is None:
        return head

    firstNode = head
    secondNode = head.next
    head = secondNode

    while True:
        temp = secondNode.next
        secondNode.next = firstNode

        if temp is None or temp.next is None:
            firstNode.next = temp
            break

        firstNode.next = temp.next
        firstNode = temp
        secondNode = temp.next

    return head

def getNodesInArray(head):
    nodes = []
    while head is not None:
        nodes.append(head.value)
        head = head.next
    return nodes
