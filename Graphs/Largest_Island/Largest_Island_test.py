"""
Largest Island
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only es and 1 s.
Each 1 represents water, and each represents part of a land mass. A land mass consists of any number of es
that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacentes forming a
land mass determine its size.
Note that a land mass can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
it can be L-shaped, for example.
Write a function that returns the largest possible land mass size after changing exactly one 1 to a
given matrix will always contain at least one 1, and you may mutate the matrix.

Sample Input
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

Sample Output
6
// The 1 at row index 0 and column index 2 can be changed to a 1 to connect to the other 1s and form a land mass of size 6:

// [
    '1', 0, '0', 1, 0,
    '1', 0, '1', 0, 0,
    '0', 0, '1', 0, 1,
    '1', 0, '1', 0, 1,
    '1', 0, '1', '1', 0,
]
""" 


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [ 0, 1, 1,], [0, 0, 0], [1, 1, 0]
        expected = 5
        self.assertEqual(ProgrammingError.largestIsland(input), expected)


    


if __name__ == "__main__":
    unittest.main()

# Time: O(n*m)