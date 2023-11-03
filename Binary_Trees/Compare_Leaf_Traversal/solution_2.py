"""
Write a function that takes in the root nodes of two Binary Trees and returns a boolean representing whether their leaf traversals are the same. 
The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. A leaf node is any node that has no left or right children. 
For example, the leaf traversal of the following Binary Tree is 1, 3, 2 . 


Sample Input:
tree1 =

        1
         / \
        2   3
         /   / \
        4   6   7
         / \   \
        9   10  8

tree2 =   1
            / \
          2   3
                /   / \
                 4   6   7
                        / \   \
                       9   10  8

Sample Output:
true


"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right


# O(n + m) time | O(n + m) space
def compareLeafTraversal(tree1, tree2):
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)

    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False
        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right

    return list1CurrentNode is None and list2CurrentNode is None


def connectLeafNodes(node, previousNode=None, leafNodesLinkedList=None):
    if node is None:
        return leafNodesLinkedList, previousNode
    if node.left is None and node.right is None:
        if leafNodesLinkedList is None:
            leafNodesLinkedList = node
        if previousNode is not None:
            previousNode.right = node
        previousNode = node
    leafNodesLinkedList, previousNode = connectLeafNodes(node.left, previousNode, leafNodesLinkedList)
    leafNodesLinkedList, previousNode = connectLeafNodes(node.right, previousNode, leafNodesLinkedList)
    return leafNodesLinkedList, previousNode




# O(n + m) time | O(h1 + h2) space

