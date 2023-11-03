"""Write a function that takes in a non-empty, unordered array of positive Integers and returns the array's
majority element without sorting the array and without using more than constant space.
An array's majority element is an element of the array that appears in over half of its indices. Note that the
most common element of an array (the element that appears the most times in the array) isn't necessarily the
array's majority element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 13 both have 2 as
their most common element, yet neither of these arrays have a majority element, because neither 2 nor any
other element appears in over half of the respective arrays' indices.
You can assume that the input array will always have a majority element.


Sample Input
array= [1, 2, 3, 2, 2, 1, 2]

Sample Output

2   // 2 appears more than 3 times in the input array, and no other number appears more than 3 times in the input array.



"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.majorityElement([1, 2, 3, 2, 2, 1, 2]), 2)