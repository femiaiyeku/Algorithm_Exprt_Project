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


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = ProgrammingError.Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])


if __name__ == "__main__":
    unittest.main()


    
        


