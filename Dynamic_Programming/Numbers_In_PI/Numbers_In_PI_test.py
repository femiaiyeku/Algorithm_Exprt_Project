"""
Given a string representation of the first n d1g1ts of Pi and a 11st of positive integers (all 1n string format), 
write a function that returns the smallest number of spaces that can be added to the n d1g1ts of P1 such that all resulting numbers are found 1n the list of integers. 
Note that a single number can appear multiple times 1n the resulting numbers. For example, 1f P1 1s "3141" and the numbers are [" l", "3", "4"] , 
the number "l" 1s allowed to appear twice 1n the 11st of resulting numbers after three spaces are added: "3 I 1 I 4 I l" 
If no number of spaces to be added exists such that all resulting numbers are found 1n the 11st of integers, the function should return -1 


Sample Input
pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]

Sample Output
2 // "314159265 | 35897932384626433832 | 79"


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        pi = "3141592653589793238462643383279"
        numbers = [
            "314159265358979323846",
            "26433",
            "8",
            "3279",
            "314159265",
            "35897932384626433832",
            "79",
        ]
        self.assertEqual(ProgrammingError.numbersInPi(pi, numbers), 2)
