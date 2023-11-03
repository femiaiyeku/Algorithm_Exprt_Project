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

from collections import defaultdict, deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

    def findNodesDistanceK(self, target, k):
        adj = defaultdict(list)
        def tree_to_graph(root):
            if root.left:
                adj[root.value].append(root.left.value)
                adj[root.left.value].append(root.value)
                tree_to_graph(root.left)
            if root.right:
                adj[root.value].append(root.right.value)
                adj[root.right.value].append(root.value)
                tree_to_graph(root.right)


        tree_to_graph(self)
        visited = set()
        queue = deque([(target, 0)])
        res = []
        while queue:
            node, distance = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if distance == k:
                res.append(node)
            for neighbor in adj[node]:
                queue.append((neighbor, distance + 1))
        return res


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.right = BinaryTree(6)
    tree.right.right.left = BinaryTree(7)
    tree.right.right.right = BinaryTree(8)
    target = 3
    k = 2
    print(tree.findNodesDistanceK(target, k))


    