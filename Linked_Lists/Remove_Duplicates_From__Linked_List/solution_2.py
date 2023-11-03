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

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space - where n is the number of nodes in the Linked List

def removeDuplicatesFromLinkedList(linkedList):
    list = linkedList(linkedList.value)

    if linkedList.next != None:
        list.next = removeDuplicatesFromLinkedList(linkedList.next)
        if list.value == list.next.value:
            list.next = list.next.next
    return list

