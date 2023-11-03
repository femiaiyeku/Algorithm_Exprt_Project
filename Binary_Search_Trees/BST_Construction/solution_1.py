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


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def insert(self, value):
    if value < self.value:
        if self.left is None:
            self.left = BST(value)
        else:
            self.left.insert(value)
    else:
        if self.right is None:
            self.right = BST(value)
        else:
            self.right.insert(value)
    return self


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def contains(self, value):
    if value < self.value:
        if self.left is None:
            return False
        else:
            return self.left.contains(value)
    elif value > self.value:
        if self.right is None:
            return False
        else:
            return self.right.contains(value)
    else:
        return True
    

# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def remove(self, value, parentNode=None):
    if value < self.value:
        if self.left is not None:
            self.left.remove(value, self)
    elif value > self.value:
        if self.right is not None:
            self.right.remove(value, self)
    else:
        if self.left is not None and self.right is not None:
            self.value = self.right.getMinValue()
            self.right.remove(self.value, self)
        elif parentNode is None:
            if self.left is not None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            elif self.right is not None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            else:
                pass
        elif parentNode.left == self:
            parentNode.left = self.left if self.left is not None else self.right
        elif parentNode.right == self:
            parentNode.right = self.left if self.left is not None else self.right

    return self


def getMinValue(self):
    if self.left is None:
        return self.value
    else:
        return self.left.getMinValue()


BST.insert = insert
BST.contains = contains
BST.remove = remove
BST.getMinValue = getMinValue


