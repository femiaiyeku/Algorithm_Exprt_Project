"""
Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and 
returns the number of squares that can be formed by these coordinates. 
A square must have its four corners amongst the coordinates in order to be counted. 
A single coordinate can be used as a corner for multiple different squares. 
You can also assume that no coordinate will be farther than 100 units from the origin. 

Sample Input

points = [
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (4, 3),
]

Sample Output

8   // The 8 squares are:
    // 1: (1, 1), (1, 2), (2, 1), (2, 2)
    // 2: (1, 2), (1, 3), (2, 2), (2, 3)
    // 3: (2, 1), (2, 2), (3, 1), (3, 2)
    // 4: (2, 2), (2, 3), (3, 2), (3, 3)
    // 5: (1, 1), (1, 2), (1, 3), (2, 3)
    // 6: (1, 2), (1, 3), (1, 4), (2, 4)
    // 7: (2, 1), (2, 2), (2, 3), (3, 3)
    // 8: (2, 2), (2, 3), (2, 4), (3, 4)
    


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        points = [
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
            (1, 3),
            (2, 3),
            (3, 1),
            (3, 2),
            (3, 3),
            (4, 1),
            (4, 2),
            (4, 3),
        ]
        expected = 8
        self.assertEqual(ProgrammingError.countSquares(points), expected)