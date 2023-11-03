"""

Write three functions that take in a Binary Search Tree (BST) and an empty array, traverse the BST, 
add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, 
and post-order tree­traversal techniques, respectively. If you're unfamiliar with tree-traversal techniques, we recommend watching the Conceptual 
Overview section of this question's video explanation  before starting to code. 
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of ever/ node to its right; and its children nodes are either valid BST nodes themselves or None / null. 


Sample Input:

tree = 10
        / \ 
         5  15
        / \  / \
         2  5 13 22
        /       \   
         1        14

Sample Output:

inOrderTraverse: [1, 2, 5, 5, 10, 13, 14, 15, 22]
preOrderTraverse: [10, 5, 2, 1, 5, 15, 13, 14, 22]
postOrderTraverse: [1, 2, 5, 5, 14, 13, 22, 15, 10]


"""

def inOrderTraverse(t, a=None):
    return [inOrderTraverse(t.left, a), a.append(t.value), inOrderTraverse(t.right, a)] if t else a

def preOrderTraverse(t, a=None):
    return [a.append(t.value), preOrderTraverse(t.left, a), preOrderTraverse(t.right, a)] if t else a

def postOrderTraverse(t, a=None):
    return [postOrderTraverse(t.left, a), postOrderTraverse(t.right, a), a.append(t.value)] if t else a

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
 