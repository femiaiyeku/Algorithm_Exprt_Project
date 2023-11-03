"""
You're given three nodes that are contained in the same Binary Search Tree: nodeOne , node Two , and node Three . 
Write a function that returns a boolean representing whether one of nodeOne or node Three is an ancestor of node Two and the other node is a descendant of nodeTwo . For example,
if your function determines that nodeOne is an ancestor of nodeTwo , then it needs to see if node Three is a descendant of node Two . If your function determines that node Three is an ancestor, 
then it needs to see if nodeOne is a descendant. 
A descendant of a node N is defined as a node contained in the tree rooted at N . 
A node N is an ancestor of another node M if M is a descendant of N . 
It isn't guaranteed that nodeOne or node Three will be ancestors or descendants of node Two ,
 but it is guaranteed that all three nodes will be unique and will never be None / null . 
In other words, you'll be given valid input nodes. Each BST node has an integer value , a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / 
null. 


Sample Input
tree =    5
        /   \
         2     7
        / \   / \
         1   4 6   8
         /   /
         0   3

nodeOne = 5
nodeTwo = 2
nodeThree = 3

Sample Output

true


"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = ProgrammingError.BST(5)
        root.left = ProgrammingError.BST(2)
        root.left.left = ProgrammingError.BST(1)
        root.left.left.left = ProgrammingError.BST(0)
        root.left.right = ProgrammingError.BST(4)
        root.left.right.left = ProgrammingError.BST(3)
        root.right = ProgrammingError.BST(7)
        root.right.left = ProgrammingError.BST(6)
        root.right.right = ProgrammingError.BST(8)
        nodeOne = root
        nodeTwo = root.left
        nodeThree = root.left.right
        self.assertTrue(ProgrammingError.validateThreeNodes(root, nodeOne, nodeThree))
        

