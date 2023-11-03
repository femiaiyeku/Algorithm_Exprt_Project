"""
Write a function that takes 1n an array of integers and returns the largest possible value for the expression 
array[a] - array[b] + array[c] - array[d] ,where a, b, c ,and d areindices ofthe array and a< b < c < d

if  the input array has fewer than 4 elements, your function should return 0

Sample Input

array = [3, 6, 1, -3, 2, 7]


Sample Output

4 // by choosing a = 1, b = 3, c = 4, and d = 5


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [3, 6, 1, -3, 2, 7]
        expected = 4
        self.assertEqual(ProgrammingError.maximizeExpression(array), expected)


if __name__ == "__main__":
    unittest.main()


    