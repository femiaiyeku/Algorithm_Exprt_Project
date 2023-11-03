"""
Write a function that takes 1n a non-empty array of integers and returns the greatest sum that can be generated from a strictly-1ncreas1ng subsequence 
In the array as well as an array of the numbers 1n that subsequence. 
A subsequence of an array 1s a set of numbers that aren't necessarily adJacent 1n the array but that are 1n the same order as they appear in the array.
For instance, the numbers [l, 3, 4] form a subsequence of the array [l, 2, 3, 4] , and so do the numbers [2, 4] . 
Note that a single number 1n an array and the array itself are both valid subsequences of the array. 
You can assume that there will only be one increas1ng subsequence with the greatest sum. 


Sample Input:
array = [10, 70, 20, 30, 50, 11, 30]


Sample Output:
[110, [10, 20, 30, 50]]     // The subsequence [10, 20, 30, 50] is strictly 1ncreasing and yields the greatest sum: 110.



"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.maxSumIncreasingSubsequence([1]), [1, [1]])
