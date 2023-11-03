"""
Lowest Common Manager
You're given three inputs, all of which are Instances of an OrgChart class that have a directReports property
pointing to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance
that isn't anybody else's direct report), and the other two Inputs are reports in the organizational chart. The two
reports are guaranteed to be distinct.
Write a function that returns the lowest common manager to the two reports.


Sample Input:
topManager = Node A

reportOne = Node E
reportTwo = Node I

            A
           / \
          B   C
         / \ / \
        D  E F  G
       / \
      H   I

Sample Output:
Node B



"""

def getLowestCommonManager(topManager, reportOne, reportTwo):
    topManager.parent = None
    topManager.level = 0
    addParent(topManager, 1)
    
    node1 = reportOne if reportOne.level > reportTwo.level else reportTwo
    node2 = reportOne if reportOne.level < reportTwo.level else reportTwo
    diff = abs(reportOne.level - reportTwo.level)

    while diff > 0:
        node1 = node1.parent
        diff -= 1

    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1

def addParent(node, level):
    node.level = level
    for child in node.directReports:
        child.parent = node
        addParent(child, level + 1)

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
            
        def addDirectReports(self, directReports):
            for directReport in directReports:
                self.directReports.append(directReport)

# This is the class of the input org. chart.

