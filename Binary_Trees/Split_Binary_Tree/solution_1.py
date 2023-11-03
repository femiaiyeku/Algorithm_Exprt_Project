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
    desiredSubtreeSum = getTreeSum(tree) / 2
    canBeSplit = trySubtrees(tree, desiredSubtreeSum)[1]
    return desiredSubtreeSum if canBeSplit else 0


def trySubtrees(tree, desiredSubtreeSum):
    if tree is None:
        return (0, False)
    leftSubtreeSum, leftSubtreeCanBeSplit = trySubtrees(tree.left, desiredSubtreeSum)
    rightSubtreeSum, rightSubtreeCanBeSplit = trySubtrees(tree.right, desiredSubtreeSum)
    currentSubtreeSum = leftSubtreeSum + tree.value + rightSubtreeSum
    if currentSubtreeSum == desiredSubtreeSum:
        return (currentSubtreeSum, True)
    if leftSubtreeCanBeSplit:
        return (currentSubtreeSum, True)
    if rightSubtreeCanBeSplit:
        return (currentSubtreeSum, True)
    return (currentSubtreeSum, False)


def getTreeSum(tree):
    if tree is None:
        return 0
    return getTreeSum(tree.left) + tree.value + getTreeSum(tree.right)


