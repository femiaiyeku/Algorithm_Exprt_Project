"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search
algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

Sample Input:

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

target = 33

Sample Output:
3

"""


# O(n^2) time | O(1) space

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def reconstructBst(preOrderTraversalValues):
        if len(preOrderTraversalValues) == 0:
            return None

        currentValue = preOrderTraversalValues[0]
        rightSubtreeRootIdx = len(preOrderTraversalValues)

        for idx in range(1, len(preOrderTraversalValues)):
            value = preOrderTraversalValues[idx]
            if value >= currentValue:
                rightSubtreeRootIdx = idx
                break

        leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
        rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])

        return BST(currentValue, leftSubtree, rightSubtree)
    

    def preOrderTraverse(tree, array):
        if tree is not None:
            array.append(tree.value)
            preOrderTraverse(tree.left, array)
            preOrderTraverse(tree.right, array)
        return array
    



    