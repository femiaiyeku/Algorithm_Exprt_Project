"""

Write a function that takes ,n the head of a Singly Linked List and returns a boolean representing whether the linked list's nodes form a palindrome.
 Your function shouldn't make use of any aux1l1ary data structure 
A palindrome ,s usually defined as a string that's written the same forward and backward. For a linked list's nodes to form a palindrome, 
their values must be the same when read from left to right and from right to left. Note that single-character strings are palindromes, 
which means that single-node linked lists form palindromes. 
Each Linked  list node has an integer value as well as a next node po,nt,ng to the next node ,n the list or to None / null if it's the tail of the list. 
You can assume that the input linked list will always have at least one node; ,n other words. the head will never be None / null. 

Sample Input:
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 // the head node with value 0

Sample Output:
true // it's a palindrome



"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(n) space - where n is the number of nodes in the Linked List

def linkedListPalindrome(head):
    status, _ = helper(head, head)
    return status

def helper(leftNode, rightNode):
    if rightNode is None:
        return True, leftNode
    
    status, leftNodeToCompare = helper(leftNode, rightNode.next)
    status = status and leftNodeToCompare.value == rightNode.value
    leftNodeToCompare = leftNodeToCompare.next
    return status, leftNodeToCompare

# O(n) time | O(1) space - where n is the number of nodes in the Linked List

