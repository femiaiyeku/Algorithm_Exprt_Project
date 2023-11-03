"""

You're given an unordered list of unique integers nums in the range [1, n] , where n represents the length of nums + 2 . This means that two numbers in this range are missing from the list. 
Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically. 

Example:
Input:
nums = [3, 1, 4]
Output:
[2, 5]



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 1, 4]
        output = [2, 5]
        self.assertEqual(ProgrammingError.missingNumbers(input), output)



        

