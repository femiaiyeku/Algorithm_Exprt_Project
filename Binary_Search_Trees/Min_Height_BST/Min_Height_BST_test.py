"""
Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST. 
The function should minimize the height of the BST.  You've been provided with a BST class that you'll have to use to construct the BST. 
Each BST node has an integer value , a left child node, and a right child node. A node is said to be a valid BST node 
if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / 
null. A BST is valid if and only if all of its nodes are valid BST nodes. 
Note that the BST class already has an insert method which you can use if you want. 

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

Sample Output
            10
            /    \
              2      14
            /   \   /   \
            1     5  13   15
                    \       \
                    7       22

            // This is one example of a BST with min height
            // that you could create from the input array.
            // You could create other BSTs with min height
            // from the same array; for example:
            //            10
            //          /     \
            //        5        15
            //      /   \     /   \
            //     2     7   13   22
            //   /           \
            //  1            14
"""


from sqlite3 import ProgrammingError
import unittest
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))
def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
def getTreeHeight(tree, height = 0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = ProgrammingError.minHeightBst(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])
        self.assertEqual(inOrder, sorted(array))



