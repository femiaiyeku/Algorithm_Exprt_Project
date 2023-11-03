"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth. 
Write a function that takes in a Binary Tree and returns the sum of all of its subtrees· nodes· depths. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null


Sample Input:
tree = 1
        / \
        2   3
        / \ / \
        4  5 6  7
         / \
        8  9


Sample Output:
26


// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// The depth of the node with value 6 is 2.
// The depth of the node with value 7 is 2.
// The depth of the node with value 8 is 3.
// The depth of the node with value 9 is 3.
// Therefore, the sum of all of the nodes' depths is 1


"""


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
# Solution 1: O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree

def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

    numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths

    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)



class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths


