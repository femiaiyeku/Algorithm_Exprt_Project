"""
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a
palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character
strings are palindromes.
Sample Input

string = "abcdcba"

Sample Output

true // it's written the same forward and backward


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.isPalindrome("a"), True)

