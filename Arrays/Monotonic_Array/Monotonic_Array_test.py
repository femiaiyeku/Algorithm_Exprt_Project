"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic. 
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing. 
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease. 
Note that empty arrays and arrays of one element are monotonic. 

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
true


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):

        self.assertEqual(ProgrammingError.isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]), True)
        self.assertEqual(ProgrammingError.isMonotonic([]), True)
        self.assertEqual(ProgrammingError.isMonotonic([1]), True)
        self.assertEqual(ProgrammingError.isMonotonic([1, 2]), True)
        self.assertEqual(ProgrammingError.isMonotonic([2, 1]), True)
        self.assertEqual(ProgrammingError.isMonotonic([1, 5, 10, 1100, 1101, 1102, 9001]), True)

        