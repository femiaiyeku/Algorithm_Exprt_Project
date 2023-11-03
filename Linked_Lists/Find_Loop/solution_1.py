"""
Write a function that takes in the head of a Singly Linked List that contains a loop {in other words, the list's tail node points to some node in the list instead of None / null ). The function should return the node {the actual node--not just its value) from which the loop originates in consta1t space. 
Each Linked list node has an irteger value as well as a next node pointing to the next node in the list. 

Sample Input:
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 2
// 6 is connected to 3
Sample Output:
4 -> 5 -> 6 // the node with value 3
// 6 is connected to 3, so 3 is the node that the input Linked List loops from
// Note: that the input Linked List may not always have a loop
// and may terminate in a None / null value
// Also note: that the target node may be the first node in the list
// Note: Do not edit the linked list


"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next

    return first

# Time Complexity: O(n)