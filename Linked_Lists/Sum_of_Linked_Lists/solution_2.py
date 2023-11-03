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

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) time | O(max(n, m)) space

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    l1 = linkedListOne
    l2 = linkedListTwo
    dummy = LinkedList(None)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.value if l1 else 0
        v2 = l2.value if l2 else 0
        carry, value = divmod(v1 + v2 + carry, 10)
        current.next = LinkedList(value)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# O(max(n, m)) time | O(max(n, m)) space

