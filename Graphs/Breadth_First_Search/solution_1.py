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
    
    # Time Complexity: O(v + e)
    # Space Complexity: O(v)
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
    


if __name__ == "__main__":
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    expected = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    actual = graph.breadthFirstSearch([])
    print(actual)
    assert actual == expected

    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
    graph.children[0].addChild("E").addChild("F").addChild("O")
    graph.children[1].addChild("P")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[0].addChild("Q").addChild("R")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    graph.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
    graph.children[4].children[0].addChild("W").addChild("X")
    graph.children[4].children[0].children[1].addChild("Y").addChild("Z")

    expected = ["A", "B", "C", "D", "L", "M", "E", "F", "O", "P", "G", "H", "Q", "R", "I", "J", "K", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    actual = graph.breadthFirstSearch([])

    
