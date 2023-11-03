"""

Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node. 
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null

Sample Input

tree =    1
         /     \
         2       3
        /  \    /  \
        4    5  6    7
        / \
       8   9



Sample Output

tree =    1
            /     \
            3       2
            /  \    /  \
            7    6  5    4
                        / \
                       9   8




"""


from sqlite3 import ProgrammingError
import unittest


from Invert_Binary_Tree import BinaryTree

def insert(self, value):
    current = self
    while True:
        if value < current.value:
            if current.left is None:
                current.left = ProgrammingError.BinaryTree(value)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = ProgrammingError.BinaryTree(value)
                break
            else:
                current = current.right
    return self


def testTree(self):
    test = ProgrammingError.BinaryTree(1).insert(2).insert(3).insert(4).insert(5).insert(6).insert(7).insert(8).insert(9)
    invertedTest = ProgrammingError.BinaryTree(1).insert(3).insert(2).insert(7).insert(6).insert(5).insert(4).insert(9).insert(8)
    ProgrammingError.invertBinaryTree(test)
    self.assertTrue(test.__eq__(invertedTest))

