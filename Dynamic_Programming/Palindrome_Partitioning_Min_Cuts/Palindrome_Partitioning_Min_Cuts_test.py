"""
Given a non-empty string, write a function that returns the minimum number of cuts needed to perform on the string
such that each remaining substring is a palindrome.
A palindrome is defined as a string that's written the same forward as backward. Note that single-character strings are
palindromes

Sample Input:

string = "noonabbad"

Sample Output:

2 // noon | abba | d



"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.palindromePartitioningMinCuts("a"), 0)
