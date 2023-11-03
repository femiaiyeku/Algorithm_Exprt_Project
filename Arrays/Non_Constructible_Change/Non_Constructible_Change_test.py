"""
Given an array of positive integers representing the values of coins in your possession, 
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. 
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value). 
For example, if you're given coins = [l, 2, S] , the minimum amount of change that you can't create is 4 .
 If you're given no coins, the minimum amount of change that you can't create is 1 . 


Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output
20


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]), 20)
