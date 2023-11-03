"""
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating rhr1rr1rtPr 
The first non-repeating character i􀀖 the first character in a string that occurs only once. 
If the input string doesn't have any non-repeating characters, your function should return -1 . 


Sample Input


string = "abcdcaf"


Sample Output


1 // The first non-repeating character is "b" and is found at index 1.


"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        self.assertEqual(ProgrammingError.firstNonRepeatingCharacter(input), expected)


if __name__ == "__main__":
    unittest.main()

    
