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



from sqlite3 import ProgrammingError
import unittest



class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = ProgrammingError.LinkedList(0)
        test.next = ProgrammingError.LinkedList(1)
        test.next.next = ProgrammingError.LinkedList(2)
        test.next.next.next = ProgrammingError.LinkedList(3)
        test.next.next.next.next = ProgrammingError.LinkedList(4)
        test.next.next.next.next.next = ProgrammingError.LinkedList(5)
        self.assertEqual(ProgrammingError.middleNode(test), test.next.next.next)
        self.assertEqual(ProgrammingError.middleNode(test).value, 3)

    def test_case_2(self):
        test = ProgrammingError.LinkedList(0)
        test.next = ProgrammingError.LinkedList(1)
        test.next.next = ProgrammingError.LinkedList(2)
        test.next.next.next = ProgrammingError.LinkedList(3)
        test.next.next.next.next = ProgrammingError.LinkedList(4)
        self.assertEqual(ProgrammingError.middleNode(test), test.next.next)
        self.assertEqual(ProgrammingError.middleNode(test).value, 2)

        

