"""

Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node) and traverses
it iteratively using the in-order tree-traversal technique; the traversal should specifically not use recursion. As the tree is
being traversed, a callback function passed in as an argument to the main function should be called on each node (i.e.,
callback(currentNode)).
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input:

tree =    1
        /   \
        2     3
        /   \  / \
        4     6  7
          \
            9
callback = someCallbackFunction

Sample Output:

[4, 9, 2, 6, 1, 3, 7] // the order in which the callback function is called on the nodes

// The tree from the sample input is:
//        1
//      /   \    <-- parent-child relationships
//     2     3
//    / \   / \
//   4   6 7   null
//    \
//     9

// The callback function is called in the following order on the nodes of the tree:
// someCallbackFunction(4)
// someCallbackFunction(9)
// someCallbackFunction(2)
// someCallbackFunction(6)
// someCallbackFunction(1)
// someCallbackFunction(3)
// someCallbackFunction(7)


"""


from sqlite3 import ProgrammingError
import unittest

class BinaryTree:
      def __init__(self, value, parent=None):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None
            self.parent = parent



      def iterativeInOrderTraversal(tree, callback):
            previousNode = None
            currentNode = tree
            while currentNode is not None:
                  if previousNode is None or previousNode == currentNode.parent:
                        if currentNode.left is not None:
                              nextNode = currentNode.left
                        else:
                              callback(currentNode)
                              nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
                  elif previousNode == currentNode.left:
                        callback(currentNode)
                        nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
                  else:
                        nextNode = currentNode.parent
                  previousNode = currentNode
                  currentNode = nextNode
                  def testCallback(testArray, tree):
                    if tree is None:
                         return
                    testArray.append(tree.value)






class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, root)
        root.left.left = BinaryTree(4, root.left)
        root.left.left.right = BinaryTree(9, root.left.left)
        root.right = BinaryTree(3, root)
        root.right.left = BinaryTree(6, root.right)
        root.right.right = BinaryTree(7, root.right)
        expected = [4, 9, 2, 6, 1, 3, 7]
        actual = []
        BinaryTree.iterativeInOrderTraversal(root, lambda x: actual.append(x.value))
        self.assertEqual(actual, expected)
        actual = [] 

          
