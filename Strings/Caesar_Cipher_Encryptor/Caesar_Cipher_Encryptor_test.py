"""
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that
returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is
the key.
Note that letters should "wrap" around the alphabet; in other words, the letter shifted by one returns the letter

Sample Input:
string = "xyz"
key = 2

Sample Output:
"zab"


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.caesarCipherEncryptor("xyz", 2), "zab")

