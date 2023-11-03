"""

Write a function that takes in a Binary Tree with at least one node and checks if that Binary Tree can be split into two Binary Trees of equal sum by removing a single edge. 
If this split is possible, return the new sum of each Binary Tree, otherwise return 0. Note that you do not need to return the edge that was removed. 
The sum of a Binary Tree is the sum of all values in that Binary Tree. 
Each BinaryTree node has an integer value , a left child node, 
and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / nul 1 . 




tree = 1
      / \
      3  -2
    / \   / \
  -6   -5 5  2
  /
  2

    Sample Output:
    6
    // 6 == 1 - 3 + -6 + 2



"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    target = calSum(tree) / 2
    for node in inOrderTraverse(tree):
        if calSum(node) == target:
            return target
    return 0

def calSum(tree):
    if tree is None:
        return 0
    return tree.value + calSum(tree.left) + calSum(tree.right)

def inOrderTraverse(tree):
    if tree is None:
        return []
    return inOrderTraverse(tree.left) + [tree] + inOrderTraverse(tree.right)


def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)






