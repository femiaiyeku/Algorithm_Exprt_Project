"""

Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree. 
A path is a collection of connected 1odes in a tree, where no node is connected to more than two other nodes. The length of a path is the number of edges between the path's first node and its last node. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null


Sample Input

tree =  1
        /   \
        3     2
        /   \
        7     4
        /       \
        8         5
        /           \
        9             6

Sample Output
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6




"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BinaryTree(1)
        root.left = ProgrammingError.BinaryTree(3)
        root.left.left = ProgrammingError.BinaryTree(7)
        root.left.left.left = ProgrammingError.BinaryTree(8)
        root.left.left.left.left = ProgrammingError.BinaryTree(9)
        root.left.right = ProgrammingError.BinaryTree(4)
        root.left.right.right = ProgrammingError.BinaryTree(5)
        root.left.right.right.right = ProgrammingError.BinaryTree(6)
        root.right = ProgrammingError.BinaryTree(2)
        self.assertEqual(ProgrammingError.binaryTreeDiameter(root), 6)

