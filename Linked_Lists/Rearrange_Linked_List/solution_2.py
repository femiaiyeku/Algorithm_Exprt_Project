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


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    notInOrderHead = LinkedList(None)
    inOrderHead = LinkedList(None)
    correctHead = LinkedList(None)
    inOrderHead.next = head
    inOrderHeadDupe = inOrderHead
    notInOrderHeadDupe = notInOrderHead
    correctHeadDupe = correctHead

    while inOrderHead.next is not None:
        if inOrderHead.next.value < k:
            notInOrderHead.next = inOrderHead.next
            notInOrderHead = notInOrderHead.next
            inOrderHead.next = inOrderHead.next.next
        elif inOrderHead.next.value > k:
            correctHead.next = inOrderHead.next
            correctHead = correctHead.next
            inOrderHead.next = inOrderHead.next.next
        else:
            inOrderHead = inOrderHead.next

    notInOrderHead.next = correctHeadDupe.next
    return notInOrderHeadDupe.next


def printLinkedList(head):
    node = head
    while node is not None:
        print(node.value)
        node = node.next


if __name__ == "__main__":
    head = LinkedList(3)
    head.next = LinkedList(0)
    head.next.next = LinkedList(5)
    head.next.next.next = LinkedList(2)
    head.next.next.next.next = LinkedList(1)
    head.next.next.next.next.next = LinkedList(4)
    k = 3
    printLinkedList(rearrangeLinkedList(head, k))


# Time Complexity: O(n)
# Space Complexity: O(1)
