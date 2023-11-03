"""
Write a function that takes in an array of integers and returns an array of the same length, 
where each element in the output array corresponds to the number of integers in the input array 
that are to the right of the relevant index and that are strictly smaller than the integer at that index. 

In other words, the value at output [ i] represents the number of integers that are to the right of smallerthan input[i] . 

More formally, the value at output[i] is equivalent to the number of elements that are to the right of i and that are strictly smaller than input[i] .

Sample Input

array = [8, 5, 11, -1, 3, 4, 2]

Sample Output

[5, 4, 4, 0, 1, 1, 0]

// There are 5 integers smaller than 8 to the right of it.
// There are 4 integers smaller than 5 to the right of it.
// There are 4 integers smaller than 11 to the right of it.
// ...




"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [8, 5, 11, -1, 3, 4, 2] 
        expected = [5, 4, 4, 0, 1, 1, 0]
        output = ProgrammingError.rightSmallerThan(array)
        self.assertEqual(output, expected)

        