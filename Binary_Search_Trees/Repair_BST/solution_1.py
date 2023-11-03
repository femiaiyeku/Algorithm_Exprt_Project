"""
You're given a Binary Search Tree (BST) that has at least 2 nodes and that only hasnodes with unique values (no duplicate values).
 Exactly two nodes in the BST havehad their values swapped, therefore breaking the BST. 
 Write a function thatreturns a repaired version of the tree with all values on the correct nodes.Your function can mutate the original tree; 
 you do not need to create a new one.Moreover, the shape of the returned tree should be exactly the same as that of theoriginal input tree.
 Each BST node has an integer value, a left child node, and a right childnode. 
 A node is said to be a valid BST node if and only if it satisfies the BSTproperty: 
 its value is strictly greater than the values of every node to its left; 
itsvalue is less than or equal to the values of every node to its right; 
and itschildren nodes are either valid BST nodes themselves or None / null.

Sample Input

tree =  10
         /  \
         7   20
        / \  / \
        3 12 8  22
        /    \
      2      14

      
Sample Output

          10
         /  \
         7   20
        / \  / \
        3 12 8  22
        /    \
      2      14

"""

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST

def repairBst(tree):
    nodeOne = nodeTwo = prevNode = None

    def inOrderTraversal(node):
        nonlocal nodeOne, nodeTwo, prevNode
        if node is None:
            return

        inOrderTraversal(node.left)

        if prevNode is not None and prevNode.value > node.value:
            if nodeOne is None:
                nodeOne = prevNode
            nodeTwo = node

        prevNode = node

        inOrderTraversal(node.right)
        
    inOrderTraversal(tree)

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value

    return tree

# Test

