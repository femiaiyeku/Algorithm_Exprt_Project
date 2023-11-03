"""
Write a function that takes in the root nodes of two Binary Trees and returns a boolean representing whether their leaf traversals are the same. 
The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. A leaf node is any node that has no left or right children. 
For example, the leaf traversal of the following Binary Tree is 1, 3, 2 . 


Sample Input:
tree1 =

        1
         / \
        2   3
         /   / \
        4   6   7
         / \   \
        9   10  8

tree2 =   1
            / \
          2   3
                /   / \
                 4   6   7
                        / \   \
                       9   10  8

Sample Output:
true


"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right


# O(n + m) time | O(n + m) space
def compareLeafTraversal(tree1, tree2):
    tree1LeafTraversal = getLeafTraversal(tree1, [])
    tree2LeafTraversal = getLeafTraversal(tree2, [])
    return tree1LeafTraversal == tree2LeafTraversal


def getLeafTraversal(node, leafTraversal):
    if node is None:
        return leafTraversal
    if node.left is None and node.right is None:
        leafTraversal.append(node.value)
    getLeafTraversal(node.left, leafTraversal)
    getLeafTraversal(node.right, leafTraversal)
    return leafTraversal


# O(n + m) time | O(h1 + h2) space

def compareLeafTraversal(tree1, tree2):
    return getLeafTraversal(tree1, []) == getLeafTraversal(tree2, [])

def getLeafTraversal(node, leafTraversal):
    if node is None:
        return leafTraversal
    if node.left is None and node.right is None:
        leafTraversal.append(node.value)
    getLeafTraversal(node.left, leafTraversal)
    getLeafTraversal(node.right, leafTraversal)
    return leafTraversal


# O(n + m) time | O(h1 + h2) space

