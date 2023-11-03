"""
Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the
big string. The function should return an array of booleans, where each boolean represents whether the small
string at that index in the array of small strings is contained in the big string.
Note that you can't use language-built-in string-matching methods.


Sample Input
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

Sample Output
[true, false, true, true, false, true, false]

// Note: the booleans in the array don't have to be in any particular order.




"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]), [True, False, True, True, False, True, False])

