"""

Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node) and traverses
it iteratively using the in-order tree-traversal technique; the traversal should specifically not use recursion. As the tree is
being traversed, a callback function passed in as an argument to the main function should be called on each node (i.e.,
callback(currentNode)).
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input:

tree =    1
        /   \
        2     3
        /   \  / \
        4     6  7
          \
            9
callback = someCallbackFunction

Sample Output:

[4, 9, 2, 6, 1, 3, 7] // the order in which the callback function is called on the nodes

// The tree from the sample input is:
//        1
//      /   \    <-- parent-child relationships
//     2     3
//    / \   / \
//   4   6 7   null
//    \
//     9

// The callback function is called in the following order on the nodes of the tree:
// someCallbackFunction(4)
// someCallbackFunction(9)
// someCallbackFunction(2)
// someCallbackFunction(6)
// someCallbackFunction(1)
// someCallbackFunction(3)
// someCallbackFunction(7)


"""

def iterativeInOrderTraversal(tree, callback):
    visited = set()
    tmp = tree
    while tmp:
        if tmp.left and tmp.left not in visited:
            tmp = tmp.left
        else:
            callback(tmp)
            visited.add(tmp)
            if tmp.right and tmp.right not in visited:
                tmp = tmp.right
            else:
                tmp = tmp.parent


                