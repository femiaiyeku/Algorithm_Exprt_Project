"""
Write a function that takes in a Bincry Tree (where nodes have an additional pointer to their parent node) as well as a node contained in that tree and returns the given node's successor. 
A node's successor is the next node to be visited (immediately after the given node) when traversing its tree using the in-order tree-traversal technique. A node has no successor if it's the last node to be visited in the in-order traversal. 
If a node has no successor, your function should return None / nul 1 . 
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null. 



Sample Input
tree =
         1
        /   \
        2     3
       / \   
      4   5
    /
    6
node = 5

Sample Output
1


"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BinaryTree(1)
        root.left = ProgrammingError.BinaryTree(2)
        root.left.parent = root
        root.right = ProgrammingError.BinaryTree(3)
        root.right.parent = root
        root.left.left = ProgrammingError.BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = ProgrammingError.BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = ProgrammingError.BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root

        actual = ProgrammingError.findSuccessor(root, node)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


      