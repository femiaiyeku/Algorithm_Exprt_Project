from sqlite3 import ProgrammingError
import unittest

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        root = ProgrammingError.repairBst(root)
        self.assertTrue(validateBst(root))
        self.assertEqual(root.value, 10)
        self.assertEqual(root.left.value, 5)
        self.assertEqual(root.left.left.value, 2)
        self.assertEqual(root.left.left.left.value, 1)
        self.assertEqual(root.left.right.value, 5)
        self.assertEqual(root.right.value, 15)
        self.assertEqual(root.right.right.value, 22)


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    rightIsValid = validateBstHelper(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid



