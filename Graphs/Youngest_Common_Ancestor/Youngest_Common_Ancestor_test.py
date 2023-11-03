"""
You're given three inputs, all of which are instances of an Ancestral Tree class that have an ancestor property pointing to their youngest ancestor.
The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None I null ), 
and the other two inputs are descendants in the ancestral tree. 
Write a function that returns the y)ungest common ancestor to the two descendants. 
Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, 
the youngest common ancestor to nodes A and B is node A.


// The youngest common ancestor to nodes A and B is node A.
// The youngest common ancestor to nodes A and C is node A.
// The youngest common ancestor to nodes A and I is node H.
// The youngest common ancestor to nodes E and I is node H.
// The youngest common ancestor to nodes H and G is node H.
// The youngest common ancestor to nodes D and G is node A.
// This tree has five levels of depth.
// The youngest common ancestor to nodes A and E is node A.

Sample Input:

// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
    
             A
          /   \
         B     C
      /   \  /
     D     E F
    / \
      G   H I

Sample Output:

node B


"""



from sqlite3 import ProgrammingError
import unittest


class AncestralTree(ProgrammingError.AncestralTree):
     def addDescendants(self, *descendants):
          for descendant in descendants:
            class AncestralTree:
                def __init__(self, name):
                    self.name = name
                    self.ancestor = None

                def addDescendants(self, *descendants):
                    for descendant in descendants:
                        descendant.ancestor = self

            def new_trees():
                ancestralTrees = {}
                for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    ancestralTrees[letter] = AncestralTree(letter)
                return ancestralTrees

            ancestralTrees = new_trees()
            ancestralTrees["A"].addDescendants(ancestralTrees["B"], ancestralTrees["C"])
            ancestralTrees["B"].addDescendants(ancestralTrees["D"], ancestralTrees["E"])
            ancestralTrees["D"].addDescendants(ancestralTrees["G"], ancestralTrees["H"])
            ancestralTrees["C"].addDescendants(ancestralTrees["F"])
            ancestralTrees["F"].addDescendants(ancestralTrees["I"])
            topAncestor = ancestralTrees["A"]
            descendantOne = ancestralTrees["E"]
            descendantTwo = ancestralTrees["I"]
            def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
                ancestor_list_one = []
                ancestor_list_two = []
                AncestralTree.get_ancestors(ancestor_list_one, descendantOne, topAncestor)
                AncestralTree.get_ancestors(ancestor_list_two, descendantTwo, topAncestor)

                current_ancestor = None
                pointer_one = len(ancestor_list_one) - 1
                pointer_two = len(ancestor_list_two) - 1
                while pointer_one >= 0 and pointer_two >= 0:
                    if ancestor_list_one[pointer_one] == ancestor_list_two[pointer_two]:
                        current_ancestor = ancestor_list_one[pointer_one]
                        pointer_one -= 1
                        pointer_two -= 1
                    else:
                        break

                return current_ancestor

            expected = ancestralTrees["B"]
            actual = getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo)
            self.assertEqual(actual, expected)

            class AncestralTree:
                def __init__(self, name):
                    self.name = name
                    self.ancestor = None


                    def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
                        ancestor_list_one = []
                        ancestor_list_two = []
                        AncestralTree.get_ancestors(ancestor_list_one, descendantOne, topAncestor)
                        AncestralTree.get_ancestors(ancestor_list_two, descendantTwo, topAncestor)

                        current_ancestor = None
                        pointer_one = len(ancestor_list_one) - 1
                        pointer_two = len(ancestor_list_two) - 1
                        while pointer_one >= 0 and pointer_two >= 0:
                            if ancestor_list_one[pointer_one] == ancestor_list_two[pointer_two]:
                                current_ancestor = ancestor_list_one[pointer_one]
                                pointer_one -= 1
                                pointer_two -= 1
                            else:
                                break

                        return current_ancestor
                    
                    def get_ancestors(ancestor_list, descendant, topAncestor):
                        current_descendant = descendant
                        while current_descendant != topAncestor:
                            ancestor_list.append(current_descendant)
                            current_descendant = current_descendant.ancestor
                        ancestor_list.append(topAncestor)
                        return ancestor_list
            ancestralTrees = new_trees()
            ancestralTrees["A"].addDescendants(ancestralTrees["B"], ancestralTrees["C"])
            ancestralTrees["B"].addDescendants(ancestralTrees["D"], ancestralTrees["E"])
            ancestralTrees["D"].addDescendants(ancestralTrees["G"], ancestralTrees["H"])
            ancestralTrees["C"].addDescendants(ancestralTrees["F"])
            ancestralTrees["F"].addDescendants(ancestralTrees["I"])
            topAncestor = ancestralTrees["A"]
            descendantOne = ancestralTrees["E"]
            descendantTwo = ancestralTrees["I"]
            expected = ancestralTrees["B"]
            actual = getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo)
            self.assertEqual(actual, expected)
            



      