"""

You're given the head of a Singly Linked List of arbitrary length k .
 Write a function that zips the Linked List in place (i.e., doesn't create a brand new list) and returns its head. 
A Linked List is zipped if its nodes are in the following order, where k 1s the length of the Linked List: 

1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...


Each Linked List node has an integer value as well as a next node pointing to the next node in the 11st or to None I null 1f it's the tail of the list. 
You can assume that the input Linked List will always have at least one node; in other words, the head will never be None I null 

Sample Input:
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

Sample Output:
0 -> 5 -> 1 -> 4 -> 2 -> 3 // the head node with value 0


"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space - where n is the number of nodes in the Linked List

def zipLinkedList(head):
    pointer = LinkedList
    length = getLength(pointer)
    idxEndPartOneLinkedList = length // 2 if length % 2 == 0 else length // 2 + 1

    idx = 1
    while idx < idxEndPartOneLinkedList:
        pointer = pointer.next
        idx += 1

    secondHalfLinkedList = pointer.next
    pointer.next = None
    secondHalfLinkedList = reverseLinkedList(secondHalfLinkedList)

    pointer = head
    while secondHalfLinkedList is not None:
        temp = pointer.next
        pointer.next = secondHalfLinkedList
        secondHalfLinkedList = secondHalfLinkedList.next
        pointer.next.next = temp
        pointer = temp

    return head

def getLength(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length

def reverseLinkedList(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    
    return previous

def interweaveLinkedLists(list1, list2):
    list1Pointer = list1
    list2Pointer = list2
    while list1Pointer is not None and list2Pointer is not None:
        list1PointerNext = list1Pointer.next
        list2PointerNext = list2Pointer.next

        list1Pointer.next = list2Pointer
        list2Pointer.next = list1PointerNext

        list1Pointer = list1PointerNext
        list2Pointer = list2PointerNext

    return list1


if __name__ == "__main__":
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)

    zipLinkedList(head)
    print(head.value)
    print(head.next.value)
    print(head.next.next.value)
    print(head.next.next.next.value)
    print(head.next.next.next.next.value)
    print(head.next.next.next.next.next.value)


    
