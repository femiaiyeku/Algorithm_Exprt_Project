"""


he distance between a node in a Binary Tree and the tree's root is called the node's depth. 
rite a function that takes in a Binar1 Tree and returns the sum of its nodes· depths. 
ach BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None I nulL


Sample Input
tree =  1
         /  \
        2    3
         / \  / \
        4  5 6  7
         / \
        8   9

Sample Output
16

// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..

// Summing all of these depths yields 16.




"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BinaryTree(1)
        root.left = ProgrammingError.BinaryTree(2)
        root.left.left = ProgrammingError.BinaryTree(4)
        root.left.left.left = ProgrammingError.BinaryTree(8)
        root.left.left.right = ProgrammingError.BinaryTree(9)
        root.left.right = ProgrammingError.BinaryTree(5)
        root.right = ProgrammingError.BinaryTree(3)
        root.right.left = ProgrammingError.BinaryTree(6)
        root.right.right = ProgrammingError.BinaryTree(7)
        actual = ProgrammingError.nodeDepths(root)
        self.assertEqual(actual, 16)

        




