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
    return treesAreMirrored(tree.left, tree.right)


def treesAreMirrored(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None:
        return False
    elif tree1.value != tree2.value:
        return False
    else:
        return treesAreMirrored(tree1.left, tree2.right) and treesAreMirrored(tree1.right, tree2.left)
    




if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(2)
    tree.left.left = BinaryTree(3)
    tree.left.right = BinaryTree(4)
    tree.right.left = BinaryTree(4)
    tree.right.right = BinaryTree(3)
    tree.left.left.left = BinaryTree(5)
    tree.left.left.right = BinaryTree(6)
    tree.right.right.left = BinaryTree(6)
    tree.right.right.right = BinaryTree(5)

    print(symmetricalTree(tree))
    