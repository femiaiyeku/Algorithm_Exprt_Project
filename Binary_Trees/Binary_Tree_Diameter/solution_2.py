"""

Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree. 
A path is a collection of connected 1odes in a tree, where no node is connected to more than two other nodes. The length of a path is the number of edges between the path's first node and its last node. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null


Sample Input

tree =  1
        /   \
        3     2
        /   \
        7     4
        /       \
        8         5
        /           \
        9             6

Sample Output
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6




"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def binaryTreeDiameter(tree):
    a = 0
    def recurse(n):
        nonlocal a
        if not n:
            return 0
        l = recurse(n.left)
        r = recurse(n.right)
        a = max(a, l + r)
        return max(l, r) + 1
    recurse(tree)
    return a


def binaryTreeDiameter(tree):
    def recurse(n):
        if not n:
            return 0, 0
        l, l_d = recurse(n.left)
        r, r_d = recurse(n.right)
        return max(l, r) + 1, max(l + r, l_d, r_d)
    return recurse(tree)[1]

