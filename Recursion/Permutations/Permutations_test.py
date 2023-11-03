"""
Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order. 
If the input array is empty, the function should return an empty array. 

Sample Input:

array = [1, 2, 3]

Sample Output:
    
    [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
    ]

    



"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = ProgrammingError.getPermutations([])
        self.assertTrue(len(perms) == 0)

    def test_case_2(self):
        perms = ProgrammingError.getPermutations([1])
        self.assertTrue(len(perms) == 1)
        self.assertTrue([1] in perms)

    def test_case_3(self):
        perms = ProgrammingError.getPermutations([1, 2])
        self.assertTrue(len(perms) == 2)
        self.assertTrue([1, 2] in perms)
        self.assertTrue([2, 1] in perms)

    def test_case_4(self):
        perms = ProgrammingError.getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

    def test_case_5(self):
        perms = ProgrammingError.getPermutations([1, 2, 3, 4])
        self.assertTrue(len(perms) == 24)
        self.assertTrue([1, 2, 3, 4] in perms)
        self.assertTrue([1, 2, 4, 3] in perms)
        self.assertTrue([1, 3, 2, 4] in perms)
        self.assertTrue([1, 3, 4, 2] in perms)
        self.assertTrue([1, 4, 3, 2] in perms)
        self.assertTrue([1, 4, 2, 3] in perms)
        self.assertTrue([2, 1, 3, 4] in perms)
        self.assertTrue([2, 1, 4, 3] in perms)
        self.assertTrue([2, 3, 1, 4] in perms)
        self.assertTrue([2, 3, 4, 1] in perms)
        self.assertTrue([2, 4, 1, 3] in perms)
        self.assertTrue([2, 4, 3, 1] in perms)
        self.assertTrue([3, 1, 2, 4] in perms)
        self.assertTrue([3, 1, 4, 2] in perms)
        self.assertTrue([3, 2, 1, 4] in perms)
        self.assertTrue([3, 2, 4, 1] in perms)
        self.assertTrue([3, 4, 1, 2] in perms)
        self.assertTrue([3, 4, 2, 1] in perms)
        self.assertTrue([4, 1, 2, 3] in perms)
        self.assertTrue([4, 1, 3, 2] in perms)
        self.assertTrue([4, 2, 1, 3] in perms)
        self.assertTrue([4, 2, 3, 1] in perms)
        self.assertTrue([4, 3, 1, 2] in perms)
        self.assertTrue([4, 3, 2, 1] in perms)  

        
