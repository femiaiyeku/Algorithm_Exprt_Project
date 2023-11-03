
"""Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The
function should merge the lists in place (.e., It shouldn't create a brand new list) and return the head of the
merged list; the merged list should be in sorted order.
Each Linked List node has an integer value as well as a next node pointing to the next node in the list or
to None null if it's the tail of the list.
You can assume that the input linked lists will always have at least one node; in other words, the heads will never
be None / null.

Sample Input:
headOne = 2 -> 6 -> 7 -> 8  // the head node with value 2

headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10  // the head node with value 1

Sample Output:

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10  // the new head node with value 1

"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space - where n is the number of nodes in the first Linked List and m is the number of nodes

def mergeLinkedLists(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo


def recursiveMerge(p1, p2, p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)


# This is the class of the input linked list.
