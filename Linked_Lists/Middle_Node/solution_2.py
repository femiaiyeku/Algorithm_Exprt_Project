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

        def middleNode(linkedList):
            fast = linkedList
            slow = linkedList
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next

            return slow
        
        # O(n) time | O(1) space
        # where n is the number of nodes in the Linked List
        