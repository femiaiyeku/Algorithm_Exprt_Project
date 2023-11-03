"""
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum. 
A branch sum is the sum of all values in a Binary Tree branch.
A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. 
Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be Bi naryTree nodes themselves or None / nul 1 . 

Sample Input
tree = 1
        / \ 
         2   3
        / \ / \
         4  5 6  7
         / \
            8 9
Sample Output
[15, 16, 18, 10, 11]
// 15 == 1 + 2 + 4 + 8
// 16 == 1 + 2 + 4 + 9
// 18 == 1 + 2 + 5 + 10
// 10 == 1 + 3 + 6
// 11 == 1 + 3 + 7



"""

from sqlite3 import ProgrammingError
import unittest
from solution_1 import BinaryTree


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test1 = BinaryTree(1)
        test1.insert([2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(ProgrammingError.branchSums(test1), [15, 16, 18, 10, 11])

class BinaryTree(BinaryTree):
        def insert(self, values, i = 0):
                if i >= len(values):
                       return
                queue = [self]
                while len(queue) > 0:
                       current = queue.pop(0)
                if current.left is None:
                        current.left = BinaryTree(values[i])
                        # break
                queue.append(current.left)
                if current.right is None:
                        current.right = BinaryTree(values[i])
                        # break
                queue.append(current.right)
                self.insert(values, i + 1)
                return self
        

