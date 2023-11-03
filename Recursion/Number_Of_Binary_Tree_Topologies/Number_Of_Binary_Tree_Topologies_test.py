"""
Write a function that takes in a non-negative integer n and returns the number of possible Binary Tree topologies that can be created with exactly n nodes. 
A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2 : a root node with a left node, and a root node with a right node. 
Note that when n is equal to 0 , there's one topology that can be created: the None I nul 1 node. 


Sample Input:
n = 3

Sample Output:
5


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.numberOfBinaryTreeTopologies(0), 1)


    def test_case_2(self):
        self.assertEqual(ProgrammingError.numberOfBinaryTreeTopologies(1), 1)
        



