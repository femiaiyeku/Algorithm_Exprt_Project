"""
Write a function that takes in a string of words separated by one or more whites paces and returns a string that has these words in reverse order. For example, given the string "tim is great" , your function should return "great is tim" 
For this problem, a word can contain special characters, punctuation, and numbers. The words 1n the string will be separated by 
one or more wh1tespaces, and the reversed string must contain the same wh1tespaces as the original string. For example, given the string "whi tespaces 4" you would be expected to return "4 whitespaces11 
Note that you're nor allowed to to use any built-in split or reverse methods/functions. However, you are allowed to use a built-in join method/function. 
Also note that the input string isn't guaranteed to always contain words 

Sample Input:
string = "AlgoExpert is the best!"

Sample Output:
"best! the is AlgoExpert"

"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.reverseWordsInString("AlgoExpert is the best!"), "best! the is AlgoExpert")

    def test_case_2(self):
        self.assertEqual(ProgrammingError.reverseWordsInString("a b c d"), "d c b a")


if __name__ == "__main__":
    unittest.main()

