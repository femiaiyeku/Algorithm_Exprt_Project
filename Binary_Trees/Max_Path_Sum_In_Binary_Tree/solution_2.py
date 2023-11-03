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

import sys

def maxPathSum(tree):
    if tree == None:
        import sys

        def maxPathSum(tree, head=True):
            if tree is None:
                return -sys.maxsize, 0
            lSum, lSumPath = maxPathSum(tree.left, head=False)
            rSum, rSumPath = maxPathSum(tree.right, head=False)
            maxSum = max(lSum, rSum, lSumPath + rSumPath + tree.value)
            maxSumPath = max(lSumPath, rSumPath) + tree.value
            return maxSum, maxSumPath if not head else maxSum
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        