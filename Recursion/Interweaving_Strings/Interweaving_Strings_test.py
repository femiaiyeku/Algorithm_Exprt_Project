"""

Write a function that takes in three strings and returns a boolean representing whether the third string can be
formed by interweaving the first two strings.
To interweave strings means to merge them by alternating their letters without any specific pattern. For instance,
the strings "abe" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23 (this list is
nonexhaustive).
Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input:
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Sample Output:
true


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(ProgrammingError.interweavingStrings(one, two, three), True)

    def test_case_2(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjo"
        self.assertEqual(ProgrammingError.interweavingStrings(one, two, three), False)

    def test_case_3(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbcbcac"
        self.assertEqual(ProgrammingError.interweavingStrings(one, two, three), True)
        



