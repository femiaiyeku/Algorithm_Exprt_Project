"""
The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and visits nodes in the following order: 
1.  Current node 
2. 	Left subtree 
3. 	Right subtree

Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree {BST), 
write a function that creates the relevant BST and returns its root node. 
The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal. 
Each BST node has an integer value, a left child node, and a right child node.
 A node is said to be a valid BST node if and only if it satisfies the BST property: 
 its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None I 
null. 

Sample Input
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

Sample Output
        10
         /  \
        4    17
         / \     \  
        2   5     19
         /          /
        1         18


"""


from sqlite3 import ProgrammingError
import unittest

BST =ProgrammingError.BST

def getDfsOrder(root, order):
    if root is None:
        return
    order.append(root.value)
    getDfsOrder(root.left, order)
    getDfsOrder(root.right, order)
    return order

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
        expected = [10, 4, 2, 1, 5, 17, 19, 18]
        actual = getDfsOrder(reconstructBst(preOrderTraversalValues), [])
        self.assertEqual(actual, expected)


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







