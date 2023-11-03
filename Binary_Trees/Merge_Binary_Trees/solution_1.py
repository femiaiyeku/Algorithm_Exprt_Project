"""
Given two binary trees, merge them and return the resulting tree. 
If two nodes overlap during the merger then sum the values, otherwise use the existing node. 
Note that your solution can either mutate the existing trees or return a new tree. 

tree1 =  1
        / \
       3   2
       /   \
       7    4

tree2 =  2
        / \
        5   9
        /   / \
        2   7  6

output =    2
            / \
            8   11
            / \  / \
            9  4 7  6 
            
            
            
 """


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Time: O(n) | Space: O(n) - where n is the number of nodes in the tree

def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)

    return tree1

 