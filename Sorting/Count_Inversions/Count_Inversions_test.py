"""
Write a function that takes in an array of integers and returns the number of inversions in the array. 
An inversion occurs if for any valid indices i and j , i < j and array[i] > array[j] 

For example, given array = [3, 4, 1, 2) , there are 4 inversions. The following pairs of indices represent inversions

Intuitively, the number of inversions is a measure of how unsorted the array is.

Sample Input
array = [2, 3, 3, 1, 9, 5, 6]

Sample Output

5

"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.countInversions([1, 2, 3, 4, 5, 6, 7]), 0)
