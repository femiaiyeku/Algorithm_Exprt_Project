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



class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



class Tree:
    valid_tree = True

    def height_of_tree(self, node, level=0):
        if self.valid_tree is False:
            return 0
        if node is None:
            return level
        left_height = self.height_of_tree(node.left, level+1)
        right_height = self.height_of_tree(node.right, level+1)
        if abs(left_height - right_height) > 1:
            self.valid_tree = False
        return max(left_height, right_height)
    
    def heightBalancedBinaryTree(tree):

        the_tree = Tree()
        the_tree.height_of_tree(tree)
        return the_tree.valid_tree
    
    