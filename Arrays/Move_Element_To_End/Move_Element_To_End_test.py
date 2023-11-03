"""
You re given an array of integers and an integer .
Write a function that moves all instances of that integer 1n the array to the end of the array and returns the array The function should perform this in place (1 e, 
1t should mutate the input array) and doesn t need to maintain the order of the other integers 

Sample Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]

Sample Output:
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 3, 2, 2, 2, 2, 2])
        
        