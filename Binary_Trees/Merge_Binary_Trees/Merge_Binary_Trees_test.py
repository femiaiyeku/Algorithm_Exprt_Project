"""
Given two binary trees, merge them and return the resulting tree. 
If two nodes overlap during the merger then sum the values, otherwise use the existing node. 
Note that your solution can either mutate the existing trees or return a new tree. 

tree1 =  1
        / \
       3   2
       /   \
       7    4

tree2 =  2
        / \
        5   9
        /   / \
        2   7  6

output =    2
            / \
            8   11
            / \  / \
            9  4 7  6 
            
            
            
"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = ProgrammingError.BinaryTree(1)
        tree1.left = ProgrammingError.BinaryTree(3)
        tree1.left.left = ProgrammingError.BinaryTree(7)
        tree1.right = ProgrammingError.BinaryTree(2)
        tree1.right.right = ProgrammingError.BinaryTree(4)
        tree2 = ProgrammingError.BinaryTree(2)
        tree2.left = ProgrammingError.BinaryTree(5)
        tree2.left.left = ProgrammingError.BinaryTree(2)
        tree2.right = ProgrammingError.BinaryTree(9)
        tree2.right.left = ProgrammingError.BinaryTree(7)
        tree2.right.right = ProgrammingError.BinaryTree(6)
        output = ProgrammingError.mergeBinaryTrees(tree1, tree2)
        self.assertEqual(output.value, 2)
        self.assertEqual(output.left.value, 8)
        self.assertEqual(output.right.value, 11)
        self.assertEqual(output.left.left.value, 9)
        self.assertEqual(output.left.right.value, 4)
        self.assertEqual(output.right.left.value, 7)
        self.assertEqual(output.right.right.value, 6)

        
 