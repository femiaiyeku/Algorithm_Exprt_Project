"""
Write a function that takes in a string and returns its longest substring without duplicate characters.
You can assume that there will only be one longest substring without duplication.

Sample Input

string = "clementisacap"

Sample Output

"mentisac"

"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.longestSubstringWithoutDuplication("clementisacap"), "mentisac")

if __name__ == "__main__":
    unittest.main()


    
