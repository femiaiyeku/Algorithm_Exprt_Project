"""
You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared
intersection node. Write a function that returns the intersection node or returns None/null if there is no
intersection.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or
to None/null if it's the tail of the list.
Note: Your function should return an existing node. It should not modify either Linked List, and it should not
create any new Linked Lists.



Sample Input:
headOne = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 2
headTwo = 10 -> 11 -> 12 -> 13 // the head node with value 12


Sample Output:
12 -> 13 // the node with value 12
// Note that the intersection node can be anywhere between the two lists and the

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        li = ProgrammingError.LinkedList(0)
        li.next = ProgrammingError.LinkedList(1)
        li.next.next = ProgrammingError.LinkedList(2)
        li.next.next.next = ProgrammingError.LinkedList(3)
        li.next.next.next.next = ProgrammingError.LinkedList(4)
        li.next.next.next.next.next = ProgrammingError.LinkedList(5)
        li.next.next.next.next.next.next = ProgrammingError.LinkedList(6)
        li2 = ProgrammingError.LinkedList(10)
        li2.next = ProgrammingError.LinkedList(11)
        li2.next.next = ProgrammingError.LinkedList(12)
        li2.next.next.next = ProgrammingError.LinkedList(13)
        li2.next.next.next.next = li.next.next.next
        self.assertEqual(ProgrammingError.intersection(li, li2), li.next.next.next)
        self.assertEqual(ProgrammingError.intersection(li2, li), li.next.next.next)

        