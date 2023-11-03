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

from sqlite3 import ProgrammingError
import unittest
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        orgCharts = getOrgCharts()
        topManager = orgCharts[0]
        reportOne = orgCharts[10]
        reportTwo = orgCharts[2]
        expected = orgCharts[0]
        actual = ProgrammingError.getLowestCommonManager(topManager, reportOne, reportTwo)
        self.assertEqual(actual, expected)

def getOrgCharts():
    orgCharts = []
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in alphabet:
        orgCharts.append(OrgChart(letter))
    orgCharts[0].addDirectReports([orgCharts[1], orgCharts[2]])
    orgCharts[1].addDirectReports([orgCharts[3], orgCharts[4]])
    orgCharts[2].addDirectReports([orgCharts[5], orgCharts[6]])
    orgCharts[3].addDirectReports([orgCharts[7], orgCharts[8]])
    orgCharts[4].addDirectReports([orgCharts[9]])
    orgCharts[6].addDirectReports([orgCharts[10]])
    return orgCharts

if __name__ == "__main__":
    unittest.main()
    

