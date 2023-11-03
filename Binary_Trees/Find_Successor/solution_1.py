"""
Write a function that takes in a Bincry Tree (where nodes have an additional pointer to their parent node) as well as a node contained in that tree and returns the given node's successor. 
A node's successor is the next node to be visited (immediately after the given node) when traversing its tree using the in-order tree-traversal technique. A node has no successor if it's the last node to be visited in the in-order traversal. 
If a node has no successor, your function should return None / nul 1 . 
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / null. 



Sample Input
tree =
         1
        /   \
        2     3
       / \   
      4   5
    /
    6
node = 5

Sample Output
1


"""



class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)



def getLeftMostChild(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def getRightMostParent(node):
    current = node
    while current.parent is not None and current.parent.right == current:
        current = current.parent
    return current.parent


