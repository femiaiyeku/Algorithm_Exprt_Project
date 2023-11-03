"""
Write a function that takes in an array of integers and returns the number of inversions in the array. 
An inversion occurs if for any valid indices i and j , i < j and array[i] > array[j] 

For example, given array = [3, 4, 1, 2) , there are 4 inversions. The following pairs of indices represent inversions

Intuitively, the number of inversions is a measure of how unsorted the array is.

Sample Input
array = [2, 3, 3, 1, 9, 5, 6]

Sample Output

5

"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftTreeSize = 0
        self.numInversions = 0

        def insertBST(root, node):
            if node.value > root.value:
                root.numInversions += root.leftTreeSize
                if root.right is None:
                    root.right = node
                else:
                    insertBST(root.right, node)
            else:
                root.leftTreeSize += 1
                if root.left is None:
                    root.left = node
                else:
                    insertBST(root.left, node)

        def countInversions(array):
            if len(array) == 0:
                return 0
            root = BST(array[0])
            for i in range(1, len(array)):
                insertBST(root, BST(array[i]))
            return root.numInversions
        

