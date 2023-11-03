"""
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Bubble Sort algorithm to sort the array. 
If you're unfamiliar with Bubble Sort, 
we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 


Sample Input: 

array = [8, 5, 2, 9, 5, 6, 3]

Sample Output:

[2, 3, 5, 5, 6, 8, 9]

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.bubbleSort([1, 2, 3]), [1, 2, 3])

        