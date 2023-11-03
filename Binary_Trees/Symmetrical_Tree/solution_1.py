"""

Write a function that takes in a Binary Tree and returns if that tree is symmetrical. A tree is symmetrical if the left and right subtrees are mirror images of each other. 
Each BinaryTree node has an irteger value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null . 

Sample Input:
tree =   1
        / \
       2   2
        / \ / \
       3  4 4  3
      / \     / \
    5    6   6   5

Sample Output:
True


"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft) > 0 and len(stackRight) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()

        if left is None and right is None:
            continue
        elif left is None or right is None:
            return False
        elif left.value != right.value:
            return False

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)


    return True


