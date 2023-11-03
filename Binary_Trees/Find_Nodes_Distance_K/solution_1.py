"""

You're given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive integer k .
 Write a function that returns the values of all the nodes that are exactly distance k from the node with target value. 
The distance between two nodes is defined as the number of edges that must be traversed to go from one node to the other.
 For example, the distance between a node and its immediate left or right child is 1 . The same holds in reverse: the distance between a node and its parent is 1 . 
 In a tree of three nodes where the root node has a left and right child, the left and right children are distance 2 from each other. 
Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Bi naryTree nodes themselves or None / nul 1 . 
Note that all BinaryTree node values will be unique, and your function can return the output values in any order. 


Sample Input
tree =   1
        /   \
        2     3
        /   \     \
        4     5    6     
                   /   \
                  7     8
target = 3
k = 2


Sample Output
[2, 7, 8]
// There are three nodes with value 2, 7, and 8 at distance 2 from node with value 3
// Note that there are two other nodes that are distance 2 from node 3:
//   - The node with value 1 is at distance 2 since it takes two "turns" to reach it from node 3.
//   - The node with value 6 is at distance 2 since it takes two "turns" to reach it from node 3.



"""


# Solution 1: O(n) time | O(n) space

class BinaryTree:
        def __init__(self, value, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
             
#O(n) time | O(n) space - where n is the number of nodes in the tree
def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)
    return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def populateNodesToParents(node, nodesToParents, parent=None):
    if node is not None:
        nodesToParents[node.value] = parent
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)

def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree
    nodeParent = nodesToParents[value]
    if nodeParent.left is not None and nodeParent.left.value == value:
        return nodeParent.left
    return nodeParent.right


def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)
        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK
        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))
    return []


