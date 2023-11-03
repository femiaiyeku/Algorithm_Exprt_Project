"""
You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer. 
All leaf nodes in the tree represent operands, which will always be positive integers. All of the other nodes represent operators. There are 4 operators supported, each of which is represented by a negative integer: 



-	1 : Addition operator, adding the left and right subtrees. 
-	2 : Subtraction operator, subtracting the right subtree from the left subtree. 
-	3 : Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero. 
-	4 : Multiplication operator, multiplying the left and right subtrees. 



You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol, meaning the bonom of the tree is always evaluated first, regardless of the operator. 



Sample Input

tree =  -1
         /  \
        -2  -3
         / \  / \   
        -4  2 8 3
       / \
      2  3   

Sample Output

6



"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = ProgrammingError.BinaryTree(-1)
        tree.left = ProgrammingError.BinaryTree(-2)
        tree.right = ProgrammingError.BinaryTree(-3)
        tree.left.left = ProgrammingError.BinaryTree(-4)
        tree.left.right = ProgrammingError.BinaryTree(2)
        tree.right.left = ProgrammingError.BinaryTree(8)
        tree.right.right = ProgrammingError.BinaryTree(3)
        tree.left.left.left = ProgrammingError.BinaryTree(2)
        tree.left.left.right = ProgrammingError.BinaryTree(3)
        self.assertEqual(ProgrammingError.evaluateExpressionTree(tree), 6)



            
