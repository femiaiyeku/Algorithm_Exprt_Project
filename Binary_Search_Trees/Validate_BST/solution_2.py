"""
Write a function that takes in a potentially invalid Binary Search Tree (BSTI and returns a boolean representing whether the BST is valid. 
Each BST node has an integer value , a left child node, and a r-ight child node. A node is said to be a valid BST node 1f and only if 1t satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null. 
A BST is valid 1f and only if all of its nodes are valid BST nodes. 


Sample Input:

tree = 10
        / \ 
         5  15
        / \  / \
         2  5 13 22
        /       \   
         1        14

Sample Output: True


"""

def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        def validateBst(tree, leftParent=None, rightParent=None):
            if tree is None:
                return True
            if leftParent is not None and tree.value >= leftParent.value:
                return False
            if rightParent is not None and tree.value < rightParent.value:
                return False
            leftIsValid = validateBst(tree.left, leftParent, tree)
            return leftIsValid and validateBst(tree.right, tree, rightParent)
        
        def validateBstHelper(tree, minValue, maxValue):
            if tree is None:
                return True
            if tree.value < minValue or tree.value >= maxValue:
                return False
            leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
            return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
   