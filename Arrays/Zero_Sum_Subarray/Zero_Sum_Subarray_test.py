"""
You're given a list of intergers nums.Write a function that returns a boolean representing wehether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray whose elements sum up to 0..A subarray is a contiguous part of an array.For the purpose of this question,
a subarray can be as small as one element and as long as the original array.


Sample Input
nums = [-5, -5. 2, 3, -2]

Sample Output
True // The subarray [-5, 2, 3] sums up to 0


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.zeroSumSubarray([-5, -5, 2, 3, -2]), 3)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.zeroSumSubarray([0, 0, 0, 0, 0]), 15)


    def test_case_3(self):
        self.assertEqual(ProgrammingError.zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]), 4)

        
