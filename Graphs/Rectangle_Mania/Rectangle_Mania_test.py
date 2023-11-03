"""
Write a function that takes In a list of Cartesian coordinates {i.e., {x, y) coordinates) 
and returns the number of rectangles formed by these coordinates. 
A rectangle must have its four corners amongst the coordinates in order to be counted, 
and we only care about rectangles with sides parallel to the x and y axes 
{i.e., with horizontal and vertical sides--no diagonal sides). 
You can also assume that no coordinate will be farther than 100 units from the origin 


Sample Input
coordinates = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0]
]

Sample Output

6 // 6 rectangles can be formed by these coordinates:

// 1: [[0, 0], [0, 1], [1, 1], [1, 0]]



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0]
        ]
        self.assertEqual(ProgrammingError.rectasngleMania(coords), 6)

    def test_case_2(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, 4],
            [3, 4]
        ]
        self.assertEqual(ProgrammingError.rectasngleMania(coords), 6)

    def test_case_3(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0]
        ]
        self.assertEqual(ProgrammingError.rectasngleMania(coords), 1)

    def test_case_4(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0]
        ]
        self.assertEqual(ProgrammingError.rectasngleMania(coords), 3)
        