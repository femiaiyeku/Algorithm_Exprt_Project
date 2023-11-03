"""

Write a function that takes in an array of at least three integers and, 
without sorting the input array, returns a sorted array of the three largest integers 1n the input array. 
The function should return duplicate integers 1f necessary; for example, 1t should return [10, 18, 12] for an input array of 

[10, 5, 9, 10,12]

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output:
[18, 141, 541]


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [5, 3, -1, 5],
            [-7, 3, 7, 4],
            [12, 8, 0, 0],
            [1, -8, -8, 2],
        ]
        size = 2
        expected = 18
        actual = ProgrammingError.maximumSumSubmatrix(matrix, size)
        self.assertEqual(actual, expected)