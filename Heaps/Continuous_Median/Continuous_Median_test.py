"""
Write a ContinuousMedianHandler class that supports:
• 	The continuous insertion of numbers with the insert method. 
• 	The instant (0(1) time) retrieval of the median of the numbers that have been inserted thus far with the getMedi an method. 

The getMedian method has already been written for you. You simply have to write the insert method. 
The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest.
 If there's an odd number of numbers in the set, as in {l, 3, 7} , the median is the number in the middle ( 3 in this case); if there's an even number of numbers in the set, as in {l, 3, 7, 8} , the median is the average of the two middle numbers { 
(3 + 7) / 2 == 5 in this case) 

Sample Input:
insert(5)
insert(10)
getMedian()
insert(100)
getMedian()

Sample Output:
5
7.5

"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        handler = ProgrammingError.ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        actual = handler.getMedian()
        expected = 7.5
        self.assertEqual(actual, expected)
        handler.insert(100)
        actual = handler.getMedian()
        expected = 10

