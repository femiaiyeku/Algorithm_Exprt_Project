"""
You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List.
If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or
to None / null if it's the tail of the list.

Sample Input:

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

Sample Output:

3 -> 4 -> 5 // the head node with value 3


"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space

def middleNode(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next
    middle = count // 2
    currentNode = linkedList
    for i in range(middle):
        currentNode = currentNode.next
    return currentNode

# O(n) time | O(1) space
