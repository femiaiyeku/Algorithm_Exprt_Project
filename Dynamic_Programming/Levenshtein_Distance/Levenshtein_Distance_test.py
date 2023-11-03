"""

Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string. 
There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another. 

Sample Input: str1 = "abc", str2 = "yabd"

Sample Output: 2 // insert "y"; substitute "c" for "d"






"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.levenshteinDistance("", ""), 0)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.levenshteinDistance("", "abc"), 3)


    def test_case_3(self):
        self.assertEqual(ProgrammingError.levenshteinDistance("abc", "abc"), 0)
        
