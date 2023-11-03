"""


he distance between a node in a Binary Tree and the tree's root is called the node's depth. 
rite a function that takes in a Binar1 Tree and returns the sum of its nodes· depths. 
ach BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None I nulL


Sample Input
tree =  1
         /  \
        2    3
         / \  / \
        4  5 6  7
         / \
        8   9

Sample Output
16

// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..

// Summing all of these depths yields 16.




"""

def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepths