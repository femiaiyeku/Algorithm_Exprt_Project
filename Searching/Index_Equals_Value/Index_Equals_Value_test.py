"""

Write a function that takes in a saned array of distinct integers and returns the first index in the array that is equal to the value at
that index. In other words, your function should return the minimum index where index == array[index].
if there is no such index, your function should return -1.

Sample Input:

array = [-5, -3, 0, 3, 4, 5, 9]

Sample Output:

3

"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]), 3)


        


