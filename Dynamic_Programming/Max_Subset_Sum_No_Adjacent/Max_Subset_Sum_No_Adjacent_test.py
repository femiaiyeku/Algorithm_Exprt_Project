"""

Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array. If the input array is empty, 
the function should return e . 

Sample Input: array = [75, 105, 120, 75, 90, 135]

Sample Output: 330 // 75 + 120 + 135


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.maxSubsetSumNoAdjacent([]), 0)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.maxSubsetSumNoAdjacent([1]), 1)


    def test_case_3(self):
        self.assertEqual(ProgrammingError.maxSubsetSumNoAdjacent([1,2]), 2)

        
