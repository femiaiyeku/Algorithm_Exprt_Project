"""
Write a function that takes in a non-ernpty array of distinct integers and an integer
representing a target surn. If any two nurnbers in the input array surn up to the target surn,
the function should return thern in an array, in any order. If no two nurnbers surn up to the
target surn, the function should return an ernpty array.
Note that the target surn has to be obtained by surnrning two different integers in the
array; you can't add a single integer to itself in order to obtain the target surn.
You can assurne that there will be at rnost one pair of nurnbers surnrning up to the target
sum

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10)
sequence = [l, 6, -1, 10)

Sample Output

true

"""

#Time: O(n) | Space: O(n)

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)

