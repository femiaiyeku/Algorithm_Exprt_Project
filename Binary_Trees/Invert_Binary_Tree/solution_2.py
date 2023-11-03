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


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



#O(n) time | O(n) space - where n is the number of nodes in the Binary Tree


def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


#O(n) time | O(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree

