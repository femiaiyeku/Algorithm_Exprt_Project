"""

Write a function that, given a string, returns its longest palindromic substring.
 A palindrome 1s defined as a string thats written the same forward and backward. 
 Note that single-character strings are palindromes. 
 You can assume that there will only be one longest palindromic substring

Sample Input
string = "abaxyzzyxf"

Sample Output

"xyzzyx"

"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.longestPalindromicSubstring("a"), "a")


if __name__ == "__main__":
    unittest.main()

    
