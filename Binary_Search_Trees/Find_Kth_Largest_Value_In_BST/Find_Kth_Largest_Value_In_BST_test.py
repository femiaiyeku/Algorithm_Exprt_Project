"""
Write a function that takes in a Binary Search Tree (BST) and a positive integer k and returns the kth largest integer contained in the BST. 
You can assume that there will only' be integer values in the BST and that k is less than or equal to the number of nodes in the tree. 
Also, for the purpose of this question, duplicate integers will be treated as distinct values. In other words, 
the second largest value in a BST containing values {5, 7, 7} will be 7 -not 5 . 
Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left; 
 its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / 
null. 

Sample Input

tree =  15 
        / \ 
        5 20 
        / \ / \ 
        2 5 17 22 
        / \
        1 3

        
        k = 3

Sample Output

17


"""


from sqlite3 import ProgrammingError
import unittest

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BST(15)
        root.left = ProgrammingError.BST(5)
        root.left.left = ProgrammingError.BST(2)
        root.left.left.left = ProgrammingError.BST(1)
        root.left.left.right = ProgrammingError.BST(3)
        root.left.right = ProgrammingError.BST(5)
        root.right = ProgrammingError.BST(20)
        root.right.left = ProgrammingError.BST(17)
        root.right.right = ProgrammingError.BST(22)

        k = 3
        expected = 17
        self.assertEqual(findKthLargestValueInBst(root, k), expected)

def findKthLargestValueInBst(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return
    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)

    

