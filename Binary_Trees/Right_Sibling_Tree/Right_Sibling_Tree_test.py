"""

Write a function that takes in a Binary Tree, transforms it into a Right Sibling Tree, and returns its root. 
A Right Sibling Tree is obtained by making every node in a Binary Tree have its right property point to its right sibling instead of its right child.
 A node's right sibling is the node immediately to its right on the same level or None / null if there is no node immediately to its right. 
Note that once the transformation is complete, some nodes might no longer have a node pointing to them. For example, in the sample output below, 
the node with value 10 no longer has any inbound pointers and is effectively unreachable. 
The transformation should be done in place, meaning that the original data structure should be mutated (no new structure should be created). 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null . 



Sample Input

tree =    1
        /   \
        2     3
        / \   / \
        4   5 6   7
        / \   \    / \
        8   9   10 11 12
                /
                13


Sample Output

tree =    1
        /   \
        2     3
        / \   / \
        4   5 6   7
        / \     / \
        8   9   10 11
                /
                12
                /
                13



// The node with value 1 should have its right property set to null .
// The node with value 2 should have its right property set to the node with value 3 .
// The node with value 3 should have its right property set to null .
// The node with value 4 should have its right property set to the node with value 5 .
// The node with value 5 should have its right property set to the node with value 6 .
// The node with value 6 should have its right property set to the node with value 7 .
// The node with value 7 should have its right property set to null .
// The node with value 8 should have its right property set to the node with value 9 .
// The node with value 9 should have its right property set to the node with value 10 .
// The node with value 10 should have its right property set to the node with value 11 .
// The node with value 11 should have its right property set to the node with value 12 .
// The node with value 12 should have its right property set to the node with value 13 .
// The node with value 13 should have its right property set to null .
// Since the input Binary Tree is the same as the output Binary Tree shown above,
// you can return any node in the output tree's tree structure.


"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        ProgrammingError.rightSiblingTree(root)
        self.assertEqual(root.right, None)
        self.assertEqual(root.left.right.right.right.right, None)
        self.assertEqual(root.left.right.right.right.left, None)
        self.assertEqual(root.left.right.right.left.right, None)
        self.assertEqual(root.left.right.left.right.right, None)
        self.assertEqual(root.left.left.right.right, None)
        self.assertEqual(root.left.left.left.right, None)
        self.assertEqual(root.left.left.left.left.right, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        self.assertEqual(root.left.left.left.left.left, None)
        

class BinaryTree(ProgrammingError.BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left, right, parent)
        self.parent = parent

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = ProgrammingError.BinaryTree(values[i])
                current.left.parent = current
                break
            queue.append(current.left)
            if current.right is None:
                current.right = ProgrammingError.BinaryTree(values[i])
                current.right.parent = current
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
    


if __name__ == "__main__":
    unittest.main()

    
