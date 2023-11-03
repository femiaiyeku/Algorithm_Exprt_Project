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
    currentNode = self

    while currentNode is not None:
        if value <  currentNode.value:
            if currentNode.left is None:
                currentNode.left = BST(value)
                break
            else:
                currentNode = currentNode.left
        else:
            if currentNode.right is None:
                currentNode.right = BST(value)
                break
            else:
                currentNode = currentNode.right
    return self


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def contains(self, value):
    currentNode = self
    while currentNode is not None:
        if value < currentNode.value:
            currentNode = currentNode.left
        elif value > currentNode.value:
            currentNode = currentNode.right
        else:
            return True
    return False



# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def remove(self, value, parentNode=None):
    currentNode = self
    while currentNode is not None:
        if value < currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.left
        elif value > currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.right
        else:
            if currentNode.left is not None and currentNode.right is not None:
                currentNode.value = currentNode.right.getMinValue()
                currentNode.right.remove(currentNode.value, currentNode)
            elif parentNode is None:
                if currentNode.left is not None:
                    currentNode.value = currentNode.left.value
                    currentNode.right = currentNode.left.right
                    currentNode.left = currentNode.left.left
                elif currentNode.right is not None:
                    currentNode.value = currentNode.right.value
                    currentNode.left = currentNode.right.left
                    currentNode.right = currentNode.right.right
                else:
                    currentNode.value = None
            elif parentNode.left == currentNode:
                parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
            elif parentNode.right == currentNode:
                parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
            break
    return self


def getMinValue(self):
    currentNode = self
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode.value


def findClosestValue(self, target):
    return self.findClosestValueHelper(self, target, float("inf"))

def findClosestValueHelper(self, tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


BST.insert = insert
BST.contains = contains
BST.remove = remove
BST.getMinValue = getMinValue
BST.findClosestValue = findClosestValue
BST.findClosestValueHelper = findClosestValueHelper

# This is the class of the input tree. Do not edit.


