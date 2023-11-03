"""

Write a function that takes 1n a Binary Tree, flattens 1t, and returns its leftmost node. 
A flattened Binary Tree 1s a structure that's nearly 1dent1cal to a Doubly Linked List (except that nodes have left and right pointers instead of prev and next pointers), 
where nodes follow the original tree·s left-to-right order. 
Note that ,f the ,nput Binary Tree happens to be a valid Binary Search Tree, the nodes ,n the flattened tree will be sorted. 
The flattening should be done 1n place, meaning that the original data structure should be mutated (no new structure should be created). 
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null. 


Sample Input
tree =     5
         /     \
         2       7  
         /   \    /  \
        1     4  6    8
     /       / \
     0      3       9   


     // This tree has been flattened:
    nodeOne= 5 // the leftmost node 1n the flattened tree
    nodeTwo= 2 // the second leftmost node 1n the flattened tree
    nodeThree= 3 // the third leftmost node 1n the flattened tree
Sample Output

true  // the flattened tree's node's values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9



"""

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right


    class BinaryTree:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left 
            self.right = right

        def flattenBinaryTree(self, head=None):
            if not self:
                return head
            head = self.left.flattenBinaryTree(head)
            head = self.right.flattenBinaryTree(head)
            self.right = head
            if head:
                head.left = None
            head = self
            return head

    if __name__ == "__main__":
        root = BinaryTree(5)
        root.left = BinaryTree(2)
        root.right = BinaryTree(7)
        root.left.left = BinaryTree(1)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(0)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(8)
        root.left.right.left = BinaryTree(3)
        root.right.right.right = BinaryTree(9)
        head = root.flattenBinaryTree()
        BinaryTree.printList(head)
    
    def printList(head):
        while head:
            print(head.value, end=" ")
            head = head.right
        print()

if __name__ == "__main__":
    root = BinaryTree(5)
    root.left = BinaryTree(2)
    root.right = BinaryTree(7)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(0)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(8)
    root.left.right.left = BinaryTree(3)
    root.right.right.right = BinaryTree(9)
    head = BinaryTree.flattenBinaryTree(root)
    BinaryTree.printList(head)

    
