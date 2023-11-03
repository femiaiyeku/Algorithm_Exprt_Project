"""
You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced and false if it isn't. 
A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1 . 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null . 


Sample Input

tree =    1
        /   \
       2     3
     /   \     \
        4     5     6
             / \
            7   8

Sample Output

true



"""


# Solution 1: O(n^2) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, -1)
    
    leftSubtreeInfo = getTreeInfo(tree.left)
    rightSubtreeInfo = getTreeInfo(tree.right)

    isBalanced = (leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced) and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return TreeInfo(isBalanced, height)




def heightBalancedBinaryTree(tree):
    
    if tree is None:
        return True
    leftHeight = getHeight(tree.left)
    rightHeight = getHeight(tree.right)
    if abs(leftHeight - rightHeight) > 1:
        return False
    return heightBalancedBinaryTree(tree.left) and heightBalancedBinaryTree(tree.right)


def getHeight(tree):
    if tree is None:
        return 0
    return 1 + max(getHeight(tree.left), getHeight(tree.right))



