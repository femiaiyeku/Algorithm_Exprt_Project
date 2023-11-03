"""
You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width 1 . 
Imagine water being poured over all of the pillars; write a function that returns the surface area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored. 
You can refer to the first three minutes of this question's video explanation for a visual example. 


Sample Input

heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

Sample Output

48


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.waterArea([]), 0)


if __name__ == "__main__":
    unittest.main()


    
