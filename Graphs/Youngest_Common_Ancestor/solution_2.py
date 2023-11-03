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


 # O(d) time | O(1) space - where d is the depth (height) of the ancestral tree

class AncestralTree:
        def __init__(self, name):
            self.name = name
            self.ancestor = None

        def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
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
        
        def getDescendantDepth(self, descendant):
            depth = 0
            while descendant != self:
                depth += 1
                descendant = descendant.ancestor
            return depth
        
        def backtrackAncestralTree(self, lowerDescendant, higherDescendant, diff):
            while diff > 0:
                lowerDescendant = lowerDescendant.ancestor
                diff -= 1
            while lowerDescendant != higherDescendant:
                lowerDescendant = lowerDescendant.ancestor
                higherDescendant = higherDescendant.ancestor
            return lowerDescendant
        
        def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
            depthOne = descendantOne.getDescendantDepth(topAncestor)
            depthTwo = descendantTwo.getDescendantDepth(topAncestor)
            if depthOne > depthTwo:
                return descendantOne.backtrackAncestralTree(descendantTwo, depthOne - depthTwo)
            else:
                return descendantTwo.backtrackAncestralTree(descendantOne, depthTwo - depthOne)
            
        def getDescendantDepth(descendant, topAncestor):
            depth = 0
            while descendant != topAncestor:
                depth += 1
                descendant = descendant.ancestor
            return depth
        
        def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
            while diff > 0:
                lowerDescendant = lowerDescendant.ancestor
                diff -= 1
            while lowerDescendant != higherDescendant:
                lowerDescendant = lowerDescendant.ancestor
                higherDescendant = higherDescendant.ancestor
            return lowerDescendant
        
        