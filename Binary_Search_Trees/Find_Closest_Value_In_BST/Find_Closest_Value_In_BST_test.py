"""
Write a function that takes in a Binary Search Tree 
(Bsn and a target integer value and returns the closest value to that target value contained in the BST. 
You can assume that there will only be one closest value. 
Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strialy greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None I null. 

Sample Input:

tree = 10
        / \ 
         5  15
        / \  / \
         2  5 13 22
        /       \   
         1        14
target = 12

Sample Output:
13

"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22).insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000).insert(204).insert(205).insert(207).insert(206).insert(208).insert(203).insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
        self.assertEqual(ProgrammingError.test.findClosestValue(100), 100)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else: 
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else: 
                    currentNode = currentNode.right
        return self

    def findClosestValue(self, target):
        return self.findClosestValueHelper(self, target, float("inf"))

    def findClosestValueHelper(self, tree, target, closest):
        if tree is None:
            return closest
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            return self.findClosestValueHelper(tree.left, target, closest)
        elif target > tree.value:
            return self.findClosestValueHelper(tree.right, target, closest)
        else:
            return closest