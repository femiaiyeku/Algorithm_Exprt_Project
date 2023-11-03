"""

Write a function that takes in a pos tive integer numberOfTags and returns a list of all the valid strings that you can generate with that number of matched <div></di v> tags. 
A string is valid and contains matched <div></div> tags if for every opening tag <div> , there's a closing tag </div> that comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly numberOfTags opening tags and numberOfTags closing tags. 
For example, given numberOfTags = 2 , the valid strings to return would be: 

["<div></div><div></div>", "<div><div></div></div>"]

Note that the output strings don't need to be in any particular order.


Sample Input

numberOfTags = 3

Sample Output
    
    [
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>"
    ]

    // The strings could be ordered differently.

    // For example, the following order would also be valid:



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.generateDivTags(0), [""])

    def test_case_2(self):
        self.assertEqual(ProgrammingError.generateDivTags(1), ["<>"])

        



