"""
You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced and false if it isn't. 
A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1 . 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null . 


Sample Input

tree =    1
        /   \
       2     3
     /   \     \
        4     5     6
             / \
            7   8

Sample Output

true



"""




from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BinaryTree(1)
        root.left = ProgrammingError.BinaryTree(2)
        root.left.left = ProgrammingError.BinaryTree(4)
        root.left.left.left = ProgrammingError.BinaryTree(8)
        root.left.left.right = ProgrammingError.BinaryTree(9)
        root.left.right = ProgrammingError.BinaryTree(5)
        root.right = ProgrammingError.BinaryTree(3)
        root.right.left = ProgrammingError.BinaryTree(6)
        root.right.right = ProgrammingError.BinaryTree(7)
        self.assertEqual(ProgrammingError.heightBalancedBinaryTree(root), True)
        root.right.right.right = ProgrammingError.BinaryTree(10)
        self.assertEqual(ProgrammingError.heightBalancedBinaryTree(root), False)
        root.right.right.right.left = ProgrammingError.BinaryTree(11)
        self.assertEqual(ProgrammingError.heightBalancedBinaryTree(root), False)
        root.left.left.left.left = ProgrammingError.BinaryTree(12)
        self.assertEqual(ProgrammingError.heightBalancedBinaryTree(root), False)
        root.left.left.left.left.left = ProgrammingError.BinaryTree(13)
        self.assertEqual(ProgrammingError.heightBalancedBinaryTree(root), False)
        root.left.left.left.left.left.left = ProgrammingError.BinaryTree(14)    

if __name__ == "__main__":
    unittest.main()

    

