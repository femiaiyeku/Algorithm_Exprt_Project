"""
Write a function that takes in a string made up of brackets ((. [..). ], and )) and other optional
characters. The function should return a boolean representing whether the string is balanced with regards to
brackets.
A string is said to be balanced If It has as many opening brackets of a certain type as it has closing brackets of that
type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket
that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes afte
it. Also, brackets can't overlap each other as in [(]).

Sample Input:
string = "([])(){}(())()()"

Sample Output:
true // it's balanced



"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.balancedBrackets("()[]{}{"), False)

    def test_case_2(self):
        self.assertEqual(ProgrammingError.balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"), False)

    def test_case_3(self):
        self.assertEqual(ProgrammingError.balancedBrackets("()()[{()})]"), False)

    def test_case_4(self):
        self.assertEqual(ProgrammingError.balancedBrackets("(()())((()()()))"), True)

    def test_case_5(self):
        self.assertEqual(ProgrammingError.balancedBrackets("{}()"), True)


        