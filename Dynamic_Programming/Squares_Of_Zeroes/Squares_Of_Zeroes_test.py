"""

Write a function that takes in a square-shaped n x n two-dimensional array of only 1 s and Os and returns a boolean representing 
whether the input matrix contains a square whose borders are made up of only Os. 
Note that a 1 x 1 square doesn't count as a valid square for the purpose of this question.
 In other words, a singular e in the input matrix doesn't constitute a square whose borders are made up of only Os; a square of zeroes has to be at least 2 x 2. 


Sample Input:
matrix = [
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

Sample Output:

true



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0]
        ]
        self.assertTrue(ProgrammingError.squareOfZeroes(matrix))
     
