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





class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right
        


# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree

def rightSiblingTree(root):
    mutate(root, None, None)
    return root


def mutate(node, parent, isLeftChild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)
