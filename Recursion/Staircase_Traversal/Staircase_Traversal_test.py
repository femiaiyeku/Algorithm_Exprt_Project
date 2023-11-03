"""

You're given two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the staircase at a time. 
Write a function that returns the number of ways in which you can climb the staircase. 
For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways. You could take 1 step, 1 step, 
then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps, then 1 step. 
Note that maxSteps <= height will always be true. 

Sample Input:
height = 4
maxSteps = 2

Sample Output:

5

// There are 5 ways to climb the staircase:
// 1. 1 step + 1 step + 1 step + 1 step
// 2. 1 step + 1 step + 2 steps
// 3. 1 step + 2 steps + 1 step
// 4. 2 steps + 1 step + 1 step
// 5. 2 steps + 2 steps

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(4, 2), 5)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(10, 1), 1)

    def test_case_3(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(10, 2), 89)

    def test_case_4(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(10, 3), 274)

    def test_case_5(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(10, 4), 504)

    def test_case_6(self):
        self.assertEqual(ProgrammingError.staircaseTraversal(10, 5), 750)

        
