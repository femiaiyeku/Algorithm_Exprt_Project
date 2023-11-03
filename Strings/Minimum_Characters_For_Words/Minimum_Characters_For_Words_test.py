"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of
the words. The characters don't need to be in any particular order.
For example, the characters ["y", "r", "o", "u"] are needed to form the words
["your", "you", "or", "yo"].
Note: the input words won't contain any spaces; however, they might contain punctuation and/or special
characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]

Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]), ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"])

    def test_case_2(self):
        self.assertEqual(ProgrammingError.minimumCharactersForWords(["a", "this", "that", "did", "deed", "them!"]), ["a", "t", "t", "h", "i", "s", "d", "e", "e", "m", "!"])


if __name__ == "__main__":
    unittest.main()


# Solution 1: O(n * l) time | O(c) space - where n is the number of words, l is the length of the longest word, and c is the number of unique characters across all words


