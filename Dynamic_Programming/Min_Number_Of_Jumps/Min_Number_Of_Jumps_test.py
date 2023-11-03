"""
 Min Number Of Jumps
You're given a non-empty array of positive integers where each integer represents the maximum number of steps you
can take forward in the array. For example, if the element at index 1 is 3. you can go from index 1 to index 2, 3.
or 4.
Write a function that returns the minimum number of jumps needed to reach the final index.
Note that jumping from indexi to index 1 + x always constitutes one jump, no matter how large x is.


Sample Input

array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

Sample Output

4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
 
 """


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.minNumberOfJumps([1]), 0)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.minNumberOfJumps([1, 1]), 1)


    def test_case_3(self):
        self.assertEqual(ProgrammingError.minNumberOfJumps([3, 1]), 1)

        
