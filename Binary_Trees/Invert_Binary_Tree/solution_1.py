"""

Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node. 
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null

Sample Input

tree =    1
         /     \
         2       3
        /  \    /  \
        4    5  6    7
        / \
       8   9



Sample Output

tree =    1
            /     \
            3       2
            /  \    /  \
            7    6  5    4
                        / \
                       9   8




"""


#O(n) time | O(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

#O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
