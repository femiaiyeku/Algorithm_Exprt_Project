"""

You're given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive integer k .
 Write a function that returns the values of all the nodes that are exactly distance k from the node with target value. 
The distance between two nodes is defined as the number of edges that must be traversed to go from one node to the other.
 For example, the distance between a node and its immediate left or right child is 1 . The same holds in reverse: the distance between a node and its parent is 1 . 
 In a tree of three nodes where the root node has a left and right child, the left and right children are distance 2 from each other. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / nul 1 . 
Note that all BinaryTree node values will be unique, and your function can return the output values in any order. 


Sample Input
tree =   1
        /   \
        2     3
        /   \     \
        4     5    6     
                   /   \
                  7     8
target = 3
k = 2


Sample Output
[2, 7, 8]
// There are three nodes with value 2, 7, and 8 at distance 2 from node with value 3
// Note that there are two other nodes that are distance 2 from node 3:
//   - The node with value 1 is at distance 2 since it takes two "turns" to reach it from node 3.
//   - The node with value 6 is at distance 2 since it takes two "turns" to reach it from node 3.



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
        target = root.left
        k = 2

        expected = [4, 8, 9]
        actual = root.findNodesDistanceK(target, k)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        root = ProgrammingError.BinaryTree(1)
        root.left = ProgrammingError.BinaryTree(2)
        root.left.left = ProgrammingError.BinaryTree(4)
        root.left.left.left = ProgrammingError.BinaryTree(8)
        root.left.left.right = ProgrammingError.BinaryTree(9)
        root.left.right = ProgrammingError.BinaryTree(5)
        root.right = ProgrammingError.BinaryTree(3)
        root.right.left = ProgrammingError.BinaryTree(6)
        root.right.right = ProgrammingError.BinaryTree(7)
        target = root.left.right
        k = 2

        expected = [1, 4, 6]
        actual = root.findNodesDistanceK(target, k)
        self.assertEqual(actual, expected)

        