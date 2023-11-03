"""
You're given three nodes that are contained in the same Binary Search Tree: nodeOne , node Two , and node Three . 
Write a function that returns a boolean representing whether one of nodeOne or node Three is an ancestor of node Two and the other node is a descendant of nodeTwo . For example,
if your function determines that nodeOne is an ancestor of nodeTwo , then it needs to see if node Three is a descendant of node Two . If your function determines that node Three is an ancestor, 
then it needs to see if nodeOne is a descendant. 
A descendant of a node N is defined as a node contained in the tree rooted at N . 
A node N is an ancestor of another node M if M is a descendant of N . 
It isn't guaranteed that nodeOne or node Three will be ancestors or descendants of node Two ,
 but it is guaranteed that all three nodes will be unique and will never be None / null . 
In other words, you'll be given valid input nodes. Each BST node has an integer value , a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / 
null. 


Sample Input
tree =    5
        /   \
         2     7
        / \   / \
         1   4 6   8
         /   /
         0   3

nodeOne = 5
nodeTwo = 2
nodeThree = 3

Sample Output

true


"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

        #O(h) time | O(h) space   - where h is the height of the tree

        def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
            # Write your code here.
            return (isChild(nodeTwo, nodeOne) and isChild(nodeThree, nodeTwo)) or (isChild(nodeTwo, nodeThree) and isChild(nodeOne, nodeTwo))
            or (isChild(nodeOne, nodeThree) and isChild(nodeTwo, nodeOne))

#O(h) time | O(1) space   - where h is the height of the tree

def isChild(node, target):
    while node is not None and node != target:
        node = node.left if target.value < node.value else node.right
    return node == target


        