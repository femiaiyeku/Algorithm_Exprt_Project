"""
Write a function that takes in the root nodes of two Binary Trees and returns a boolean representing whether their leaf traversals are the same. 
The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. A leaf node is any node that has no left or right children. 
For example, the leaf traversal of the following Binary Tree is 1, 3, 2 . 


Sample Input:
tree1 =

        1
         / \
        2   3
         /   / \
        4   6   7
         / \   \
        9   10  8

tree2 =   1
            / \
          2   3
                /   / \
                 4   6   7
                        / \   \
                       9   10  8

Sample Output:
true


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = ProgrammingError.BinaryTree(1)
        tree1.left = ProgrammingError.BinaryTree(2)
        tree1.left.left = ProgrammingError.BinaryTree(4)
        tree1.left.left.left = ProgrammingError.BinaryTree(9)
        tree1.left.right = ProgrammingError.BinaryTree(10)
        tree1.right = ProgrammingError.BinaryTree(3)
        tree1.right.left = ProgrammingError.BinaryTree(6)
        tree1.right.right = ProgrammingError.BinaryTree(7)
        tree1.right.right.right = ProgrammingError.BinaryTree(8)
        tree2 = ProgrammingError.BinaryTree(1)
        tree2.left = ProgrammingError.BinaryTree(2)
        tree2.left.left = ProgrammingError.BinaryTree(4)
        tree2.left.left.left = ProgrammingError.BinaryTree(9)
        tree2.left.right = ProgrammingError.BinaryTree(10)
        tree2.right = ProgrammingError.BinaryTree(3)
        tree2.right.left = ProgrammingError.BinaryTree(6)
        tree2.right.right = ProgrammingError.BinaryTree(7)
        tree2.right.right.right = ProgrammingError.BinaryTree(8)
        self.assertEqual(ProgrammingError.compareLeafTraversal(tree1, tree2), True)

    def test_case_2(self):
        tree1 = ProgrammingError.BinaryTree(1)
        tree1.left = ProgrammingError.BinaryTree(2)
        tree1.left.left = ProgrammingError.BinaryTree(4)
        tree1.left.left.left = ProgrammingError.BinaryTree(9)
        tree1.left.right = ProgrammingError.BinaryTree(10)
        tree1.right = ProgrammingError.BinaryTree(3)
        tree1.right.left = ProgrammingError.BinaryTree(6)
        tree1.right.right = ProgrammingError.BinaryTree(7)
        tree1.right.right.right = ProgrammingError.BinaryTree(8)

        tree2 = ProgrammingError.BinaryTree(1)
        tree2.left = ProgrammingError.BinaryTree(2)
        tree2.left.left = ProgrammingError.BinaryTree(4)
        tree2.left.left.left = ProgrammingError.BinaryTree(9)
        tree2.left.right = ProgrammingError.BinaryTree(10)
        tree2.right = ProgrammingError.BinaryTree(3)
        tree2.right.left = ProgrammingError.BinaryTree(6)
        tree2.right.right = ProgrammingError.BinaryTree(7)
        tree2.right.right.right = ProgrammingError.BinaryTree(8)
        self.assertEqual(ProgrammingError.compareLeafTraversal(tree1, tree2), True)


if __name__ == "__main__":
    unittest.main()

    


