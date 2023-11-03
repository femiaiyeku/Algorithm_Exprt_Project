"""

Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, 
write a function that returns the number of ways to make change for that target amount using the given coin denominations. 
Note that an unlimited amount of coins is at your disposal. 


Sample Input: n = 6, denoms = [1, 5]

Sample Output: 2 // 1x1 + 1x5 and 6x1



"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)
