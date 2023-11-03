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
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
            
        def addDirectReports(self, directReports):
            for directReport in directReports:
                self.directReports.append(directReport)

# This is the class of the input org. chart.

# Feel free to add new properties and methods to the class.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
            
        def addDirectReports(self, directReports):
            for directReport in directReports:
                self.directReports.append(directReport)

# This is the class of the input org. chart.

# Feel free to add new properties and methods to the class.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
            
        def addDirectReports(self, directReports):
            for directReport in directReports:
                self.directReports.append(directReport)

# This is the class of the input org. chart.




