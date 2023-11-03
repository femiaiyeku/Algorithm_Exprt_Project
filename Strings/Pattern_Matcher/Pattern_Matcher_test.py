"""
You·re given two non-empty strings. The first one is a pattern consisting of only "x" sand/ or "y" s; the other one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern. 
A string S0 1s said to match a pattern 1f replacing all "x" s 1n the pattern with some non-empty substring Sl of S0 and replacing all "y" s 1n the pattern with some non-empty substring S2 of S0 yields the same string S0 
If the input stnng doesn't match the input pattern. the function should return an empty array; otherwise. 1t should return an array holding the strings Sl and S2 that represent "x" and "y" 1n the normal string, 1n that order. If the pattern doesn't contain any "x" s or "y" s, the respective letter should be represented by an empty string in the final array that you return. 
You can assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and 
"y" 1n the normal string. 


Sample Input

pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"

Sample Output

["go", "powerranger"]


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])

    def test_case_2(self):
        self.assertEqual(ProgrammingError.patternMatcher("xyxy", "abab"), ["a", "b"])

    def test_case_3(self):
        self.assertEqual(ProgrammingError.patternMatcher("yxyx", "abab"), ["b", "a"])

        