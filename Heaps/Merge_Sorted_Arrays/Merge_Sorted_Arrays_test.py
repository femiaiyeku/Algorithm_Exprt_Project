"""
Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all of
those arrays.
The integers in the merged list should be in sorted order.

Sample Input:
arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]
]

Sample Output:
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150]
        ]
        output = [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
        self.assertEqual(ProgrammingError.mergeSortedArrays(arrays), output)
