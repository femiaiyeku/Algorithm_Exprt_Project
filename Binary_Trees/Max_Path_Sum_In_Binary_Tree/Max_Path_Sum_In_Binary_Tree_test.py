"""
Write a function that takes in a Binary Tree and returns its max path sum.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes; a path
sum is the sum of the values of the nodes in a particular path.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can
either be BinaryTree nodes themselves or None / null


Sample Input:
tree =    1
        /   \
        2     3
     /   \     /  \
    4     5    6  7


Sample Output:
18
// 5 + 2 + 1 + 3 + 7




"""

from sqlite3 import ProgrammingError
import unittest

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(self, values, i=0):
    if i >= len(values):
        return
    queue = [self]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.right is None:
            current.right = BinaryTree(values[i])
            break
        queue.append(current.right)
        if current.left is None:
            current.left = BinaryTree(values[i])
            break
        queue.append(current.left)
    self.insert(values, i + 1)
    return self


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(ProgrammingError.maxPathSum(test), 18)

    