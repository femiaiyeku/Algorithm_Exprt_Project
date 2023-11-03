"""
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes
form an acyclic tree-like structure.
Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree
using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names
in the input array, and returns it.
If you're unfamiliar with Breadth-first Search, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.

Sample Input:

graph = A
         / | \
        B C D
      / \ / \
        E F G H
        / \ \
        I J K

Sample Output:

["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadFirstSearch(self, array):
        nodes = [self]
        while nodes:
            array.extend(node.name for node in nodes)
            nodes = [child for node in nodes for child in node.children]
        return array
    

