"""
Write a function that takes in an array of at least two integers and that returns an array of
the starting and ending indices of the smallest subarray in the input array that needs to be
sorted in place in order for the entire input array to be sorted (in ascending order).
If the input array is already sorted, the function should return [ -1, -1] .

Sample Input
array = [l, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

Sample Output
[ 3, 9)

"""

# Time: O(n) | Space: O(1)

from sqlite3 import ProgrammingError
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.subarraySortsubarraySort([1, 2]), [-1, -1])