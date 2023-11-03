"""

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity. 
Note that the strings are not guaranteed to only contain alphanumeric charaaers. The list you return can be in any order. 

Sample Input 

strings = ["abc", "bcd", "cbaccd"]

Sample Output
    
    ["b", "c"]


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["abc", "bcd", "cbaccd"]
        output = ["b", "c"]
        self.assertEqual(sorted(ProgrammingError.commonCharacters(strings)), output)

    def test_case_2(self):
        strings = ["a", "b", "c"]
        output = []
        self.assertEqual(sorted(ProgrammingError.commonCharacters(strings)), output)


if __name__ == "__main__":
    unittest.main()

# Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string

# Space Complexity: O(c) where c is the number of unique characters across all strings

# This is the most optimal solution because it is the most time efficient and space efficient.

