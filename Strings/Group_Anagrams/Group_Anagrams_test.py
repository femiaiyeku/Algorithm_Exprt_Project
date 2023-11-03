"""
Write a function that takes in an array of strings and groups anagrams together. 
Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams. 
Your function should return a list of anagram groups in no particular order. 


Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]




"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        output = ProgrammingError.groupAnagrams(words)
        self.assertEqual(output, expected)

    def test_case_2(self):
        words = ["cinema", "a", "flop", "iceman", "meacyne", "lofp", "olfp"]
        expected = [["cinema", "iceman"], ["a"], ["flop", "lofp", "olfp"], ["meacyne"]]
        output = ProgrammingError.groupAnagrams(words)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
    


