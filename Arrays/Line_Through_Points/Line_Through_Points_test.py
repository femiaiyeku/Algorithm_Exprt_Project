"""
You·re given an array of po,nts plotted on a 2D graph (the xy-plane). 
Write a function that returns the maximum number of points that a single line (or potentially multiple lines) on the graph passes through. 
The ,nput array will contain points represented by an array of two integers [x, y] .
 The input array will never contain duplicate points and will always contain at least one point. 

Sample Input
points = [
[-1, 0],
[0, 0],
[1, 0],
[2, 0],
[3, 0],
[3, 1],
]

Sample Output
4 // A line passes through points [-1, 0], [0, 0], [1, 0], [2, 0]



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [-1, 0],
            [0, 0],
            [1, 0],
            [2, 0],
            [3, 0],
            [3, 1],
        ]
        expected = 4
        self.assertEqual(ProgrammingError.lineThroughPoints(input), expected)
        