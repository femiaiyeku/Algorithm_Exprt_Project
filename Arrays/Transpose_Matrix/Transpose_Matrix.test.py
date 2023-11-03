"""
You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.
The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-
left to bottom-right); it switches the row and column indices of the original matrix.
You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the
same.


Sample Input
matrix = [
[1, 2],
]

Sample Output
[
[1],
[2],
]





"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        actual = ProgrammingError.transposeMatrix(matrix)
        self.assertEqual(actual, expected)