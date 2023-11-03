"""Write a BST class for a Binary Search Tree. The class should support
• 	Inserting values wrth the insert method. 
• 	Removing values wrth the remove method; thrs method should only remove the first instance of a grven value. 
• 	Searching for values with the contains method. 

Note that you can't remove values from a srngle-node tree. In other words. callrng the remove method on a srngle-node tree should simply not do anything. 
Each BST node has an rnteger value , a left child node. and a right ch rid node.
 A node rs sard to be a valrd BST node rf and only if it satrsfres the BST property:
   rts value rs strictly greater than the values of every node to rts left;
   rts value is less than or equal to the values of every node to its rrght; 
 and its children nodes are erther valid BST nodes themselves or None / null 

Sample Input:

tree = 10
        / \ 
            5  15
            / \  / \
                2  5 13 22
                /       \
                    1        14

Sample Output (after inserting 12):

tree = 10
        / \
            5  15
            / \  / \
                2  5 13 22
                /       \
                    1        14
                    /    \          
                null  12

Sample Output (after removing 10):  
tree = 12
        / \
            5  15
            / \  / \
                2  5 13 22
                /       \
                    1        14
                    /    \
                null  null

Sample Output (after searching for 15): true




"""



from sqlite3 import ProgrammingError
import unittest

BST = ProgrammingError.BST

class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        test1 = BST(10)
        test1.insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
        self.assertEqual(test1.left.value, 5)
        self.assertEqual(test1.right.right.value, 22)
        self.assertEqual(test1.right.left.value, 14)
        self.assertEqual(test1.left.right.value, 5)
        self.assertEqual(test1.left.left.value, 2)
        self.assertEqual(test1.left.left.left, None)
        test1.insert(1)
        self.assertEqual(test1.left.left.left.value, 1)

    def test_case_2(self):
        test2 = BST(10)
        test2.insert(15).insert(11).insert(22).remove(10)
        self.assertEqual(test2.contains(15), True)

    def test_case_3(self):
        test3 = BST(10)
        test3.insert(5).insert(7).insert(2).remove(10)
        self.assertEqual(test3.value, 7)
        self.assertEqual(test3.contains(10), False)







