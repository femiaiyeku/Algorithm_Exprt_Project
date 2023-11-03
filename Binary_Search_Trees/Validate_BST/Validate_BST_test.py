"""
Write a function that takes in a potentially invalid Binary Search Tree (BSTI and returns a boolean representing whether the BST is valid. 
Each BST node has an integer value , a left child node, and a r-ight child node. A node is said to be a valid BST node 1f and only if 1t satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null. 
A BST is valid 1f and only if all of its nodes are valid BST nodes. 


Sample Input:

tree = 10
        / \ 
         5  15
        / \  / \
         2  5 13 22
        /       \   
         1        14

Sample Output: True


"""

from sqlite3 import ProgrammingError
import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        self.assertEqual(ProgrammingError.validateBst(root), True)




