"""
Write a function that takes in an array of non-negative integers and returns a sorted version of that array. 
Use the Radix Sort algorithm to sort the array. 
If you're unfamiliar with Radix Sort,
 we recommend watching the Conceptual Overview seaion of this question's video explanation before starting to code 

Sample Input
array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

Sample Output

[2, 12, 65, 87, 234, 345, 654, 3008, 8762]


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.radixSort([8762, 654, 3008, 345, 87, 65, 234, 12, 2]), [2, 12, 65, 87, 234, 345, 654, 3008, 8762])


