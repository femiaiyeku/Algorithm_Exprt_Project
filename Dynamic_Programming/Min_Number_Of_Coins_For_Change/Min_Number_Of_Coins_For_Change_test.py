"""
Given an array of positive integers representing coin denominations and a single non-negative integer n representing
a target amount of money, write a function that returns the smallest number of coins needed to make change for (to
sum up to) that target amount using the given coin denominations.
Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10],
you have access to an unlimited amount of 1 s, 5 s, and 10 s.
If it's impossible to make change for the target amount, return

Sample Input: n = 7, denoms = [1, 5, 10]

Sample Output: 3 // 2x1 + 1x5


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.minNumberOfCoinsForChange(0, [2, 3, 4, 7]), 0)


if __name__ == "__main__":
    unittest.main()

    