""" Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no
particular order. If no four numbers sum up to the target sum, the function should return an empty array.
Sample Input
array = [7, 6, 4, -1, 1, 2]"

targetSum = 16
Sample Output
((7, 6, 4, -1), (7, 6, 1, 2)) """

from sqlite3 import ProgrammingError
import unittest
     
def sortAndStringify(array):
    return ','.join(sorted (list (map(lambda x: str(x), array))))

class TestProgram (unittest.TestCase):
    def test_case_1(self):
        output = ProgrammingError.fourNumberSum([7, 6, 4, -1, 1, 21], 16)
        output= list(map(sortAndStringify, output))
        quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertTrue(len (output) == 2)
        for quadruplet in quadruplets:
            self.assertTrue (sortAndStringify(quadruplet) in output)