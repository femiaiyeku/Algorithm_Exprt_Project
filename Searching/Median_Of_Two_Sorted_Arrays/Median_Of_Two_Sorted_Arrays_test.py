"""

You're given two sorted arrays of integers arrayOne and arrayTwo. Write a
function that returns the median of these arrays.
You can assume both arrays have at least one value. However, they could be of
different lengths. If the median is a decimal value, it should not be rounded
(beyond the inevitable rounding of floating point math).

Sample Input:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output:
16


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [-1, 5, 10, 20, 28, 3]
        arrayTwo = [26, 134, 135, 15, 17]
        expected = 16
        actual = ProgrammingError.medianOfTwoSortedArrays(arrayOne, arrayTwo)
        self.assertEqual(actual, expected)

