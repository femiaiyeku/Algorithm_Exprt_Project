"""
Write a function that takes a positive integer represented as a string number and an integer numDigits-
Remove numDigits from the string so that the number represented by the string is as large as possible
afterwards.
Note that the order of the remaining digits cannot be changed. You can assume numDigits will always be
than the length of number and greater than or equal to 0.

Sample Input

number = "1432219"

numDigits = 3

Sample Output
"2219"

"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.bestDigits("1432219", 3), "2219")