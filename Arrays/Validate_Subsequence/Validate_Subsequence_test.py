"""
Given two non•empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers
[l, 3, 4] form a subsequence of the array [l, 2, 3, 4] , and so do the numbers (2, 4] Note that a single number in an array and the array itself are both valid
subsequences of the array

Sample Input:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Sample Output:
true


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertEqual(ProgrammingError.isValidSubsequence(array, sequence), True)
