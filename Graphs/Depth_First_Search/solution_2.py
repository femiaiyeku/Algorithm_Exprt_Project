"""
You're given a Node class that has a name and
form an acyclic tree-like structure.
hai encoren
Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree
using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names
in the input array, and returns it.
If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's
video explanation before starting to code.

Sample Input:

graph = A
        / | \
       B  C  D
        / \   / \
       E   F G   H
        / \ \
     I   J  K

Sample Output:
    
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]



"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

        def addChild(self, name):
            self.children.append(Node(name))
            return self
        
        def get_node_names(self, node):
            return [node.name] + [name for child in node.children for name in self.get_node_names(child)]
        
        def depthFirstSearch(self, array):
            return self.get_node_names(self)
