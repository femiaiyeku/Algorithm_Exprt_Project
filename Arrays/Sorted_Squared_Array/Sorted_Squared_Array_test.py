"""
Write a function that takes 1n a non empty array of integers that are sorted 1n ascending order and 
returns a new array of the same length with the squares of the original integers also sorted 1n ascending order 

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output

[1, 4, 9, 25, 36, 64, 81]



"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]), [1, 4, 9, 25, 36, 64, 81])
        self.assertEqual(ProgrammingError.sortedSquaredArray([-10, -5, 0, 5, 10]), [0, 25, 25, 100, 100])
        self.assertEqual(ProgrammingError.sortedSquaredArray([-7, -3, 1, 9, 22, 30]), [1, 9, 49, 81, 484, 900])
        self.assertEqual(ProgrammingError.sortedSquaredArray([-10]), [100])
        self.assertEqual(ProgrammingError.sortedSquaredArray([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(ProgrammingError.sortedSquaredArray([-5, -4, -3, -2, -1]), [1, 4, 9, 16, 25])
        self.assertEqual(ProgrammingError.sortedSquaredArray([-10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])


        