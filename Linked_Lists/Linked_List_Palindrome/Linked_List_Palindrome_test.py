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

from sqlite3 import ProgrammingError
import unittest

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = ProgrammingError.LinkedList(0)
        test.next = ProgrammingError.LinkedList(1)
        test.next.next = ProgrammingError.LinkedList(2)
        test.next.next.next = ProgrammingError.LinkedList(2)
        test.next.next.next.next = ProgrammingError.LinkedList(1)
        test.next.next.next.next.next = ProgrammingError.LinkedListt(0)
        self.assertEqual(ProgrammingError.linkedListPalindrome(test), True)

    def test_case_2(self):
        test = ProgrammingError.LinkedList(0)
        test.next = ProgrammingError.LinkedList(1)
        test.next.next = ProgrammingError.LinkedList(2)
        test.next.next.next = ProgrammingError.LinkedList(1)
        test.next.next.next.next = ProgrammingError.LinkedList(0)
        self.assertEqual(ProgrammingError.linkedListPalindrome(test), True)

        


