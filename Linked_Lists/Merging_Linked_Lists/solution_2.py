"""
You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared
intersection node. Write a function that returns the intersection node or returns None/null if there is no
intersection.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or
to None/null if it's the tail of the list.
Note: Your function should return an existing node. It should not modify either Linked List, and it should not
create any new Linked Lists.



Sample Input:
headOne = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 2
headTwo = 10 -> 11 -> 12 -> 13 // the head node with value 12


Sample Output:
12 -> 13 // the node with value 12
// Note that the intersection node can be anywhere between the two lists and the

"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(1) space - where n is the number of nodes in the first Linked List and m is the number of nodes in the second Linked List
def intersection(linkedListOne,linkedListTwo):
    currentNodeOne = linkedListOne
    countOne = 0
    while currentNodeOne is not None:
        countOne += 1
        currentNodeOne = currentNodeOne.next
    currentNodeTwo = linkedListTwo
    countTwo = 0
    while currentNodeTwo is not None:
        countTwo += 1
        currentNodeTwo = currentNodeTwo.next
    if countOne > countTwo:
        return getIntersection(linkedListOne, linkedListTwo, countOne - countTwo)
    else:
        return getIntersection(linkedListTwo, linkedListOne, countTwo - countOne)
    

def getIntersection(linkedListOne, linkedListTwo, diff):
    while diff > 0:
        linkedListOne = linkedListOne.next
        diff -= 1
    while linkedListOne is not None and linkedListTwo is not None:
        if linkedListOne == linkedListTwo:
            return linkedListOne
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next
    return None

def getLen(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length

