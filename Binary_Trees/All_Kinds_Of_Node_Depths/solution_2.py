"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth. 
Write a function that takes in a Binary Tree and returns the sum of all of its subtrees· nodes· depths. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null


Sample Input:
tree = 1
        / \
        2   3
        / \ / \
        4  5 6  7
         / \
        8  9


Sample Output:
26


// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// The depth of the node with value 6 is 2.
// The depth of the node with value 7 is 2.
// The depth of the node with value 8 is 3.
// The depth of the node with value 9 is 3.
// Therefore, the sum of all of the nodes' depths is 1


"""

def allKindsOfNodeDepths(root):
    return get_all_node_depths_sum(root).total_sum

def get_all_node_depths_sum(node):
    if node is None:
        return TreeInfo(0, 0, 0)
    
    left_tree_info = get_all_node_depths_sum(node.left)
    right_tree_info = get_all_node_depths_sum(node.right)

    sum_of_left_depths = left_tree_info.sum_of_depths + left_tree_info.num_nodes_in_tree
    sum_of_right_depths = right_tree_info.sum_of_depths + right_tree_info.num_nodes_in_tree

    num_nodes_in_tree = 1 + left_tree_info.num_nodes_in_tree + right_tree_info.num_nodes_in_tree
    sum_of_depths = sum_of_left_depths + sum_of_right_depths
    total_sum = sum_of_depths + left_tree_info.total_sum + right_tree_info.total_sum

    return TreeInfo(num_nodes_in_tree, sum_of_depths, total_sum)

class TreeInfo:
    def __init__(self, num_nodes_in_tree, sum_of_depths, total_sum):
        self.num_nodes_in_tree = num_nodes_in_tree
        self.sum_of_depths = sum_of_depths
        self.total_sum = total_sum

# This is the class of the input binary tree.

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Solution 2: O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
