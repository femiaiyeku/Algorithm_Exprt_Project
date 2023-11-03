"""

Write three functions that take in a Binary Search Tree (BST) and an empty array, traverse the BST, 
add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, 
and post-order tree­traversal techniques, respectively. If you're unfamiliar with tree-traversal techniques, we recommend watching the Conceptual 
Overview section of this question's video explanation  before starting to code. 
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of ever/ node to its right; and its children nodes are either valid BST nodes themselves or None / null. 


Sample Input:

tree = 10
        / \ 
         5  15
        / \  / \
         2  5 13 22
        /       \   
         1        14

Sample Output:

inOrderTraverse: [1, 2, 5, 5, 10, 13, 14, 15, 22]
preOrderTraverse: [10, 5, 2, 1, 5, 15, 13, 14, 22]
postOrderTraverse: [1, 2, 5, 5, 14, 13, 22, 15, 10]


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

        inOrder = [1, 2, 5, 5, 10, 13, 14, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 13, 14, 22]
        postOrder = [1, 2, 5, 5, 14, 13, 22, 15, 10]

        self.assertEqual(BST.inOrderTraverse(root, []), inOrder)
        self.assertEqual(BST.preOrderTraverse(root, []), preOrder)
        self.assertEqual(BST.postOrderTraverse(root, []), postOrder)

        