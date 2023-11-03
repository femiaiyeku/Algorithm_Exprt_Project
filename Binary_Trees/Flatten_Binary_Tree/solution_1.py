"""

Write a function that takes 1n a Binary Tree, flattens 1t, and returns its leftmost node. 
A flattened Binary Tree 1s a structure that's nearly 1dent1cal to a Doubly Linked List (except that nodes have left and right pointers instead of prev and next pointers), 
where nodes follow the original tree·s left-to-right order. 
Note that ,f the ,nput Binary Tree happens to be a valid Binary Search Tree, the nodes ,n the flattened tree will be sorted. 
The flattening should be done 1n place, meaning that the original data structure should be mutated (no new structure should be created). 
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null. 


Sample Input
tree =     5
         /     \
         2       7  
         /   \    /  \
        1     4  6    8
     /       / \
     0      3       9   


     // This tree has been flattened:
    nodeOne= 5 // the leftmost node 1n the flattened tree
    nodeTwo= 2 // the second leftmost node 1n the flattened tree
    nodeThree= 3 // the third leftmost node 1n the flattened tree
Sample Output

true  // the flattened tree's node's values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9



"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#O(n) time | O(d) space where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree

def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root, [])
    for i in range(0, len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]

def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
    return array


#O(n) time | O(d) space where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree

