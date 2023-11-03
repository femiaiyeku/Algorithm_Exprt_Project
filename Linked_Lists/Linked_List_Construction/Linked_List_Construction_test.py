"""
Write doubly linked list class that has a head and a tail , both of which point to either a linked list Node or None / null . 
The class should support: 
• 	Setting the head and tail of the linked list. 
• 	Inserting nodes before and after other nodes as well as at given positions {the position of the head node is 1 ). 
• 	Removing given nodes and removing nodes with given values. 
• 	Searching for nodes with give, values. 

Note that the setHead , setTail , insertBefore , insertAfter , insertAtPosition, and remove methods all take in actual Node s as input parameters-not integers {except for insertAtPosition , which also takes in an integer representing the position); this means that you don't need to create any new Node sin these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario. 
If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language like J3va or Typescript to get a better idea of what each input parameter is. 
Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None / null . 


Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6
// Assume that we've already created the following linked list:
1 <-> 2 <-> 4 <-> 5
// All operations below are performed sequentially.
setHead(4): 4 <-> 1 <-> 2 <-> 4 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 4 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 3 <-> 6 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 3 <-> 6 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 4 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 4 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true



"""



from sqlite3 import ProgrammingError
import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.

Node = Node
if hasattr(Node, 'prev'):
    pass
else:
    Node = Node
if hasattr(Node, 'next'):
    pass
else:
    Node = Node
if hasattr(Node, 'value'):
    pass
else:
    None
Node = Node

def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values

def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values

def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


def removeNodesWithValue(linkedList, value):
    node = linkedList.head
    while node is not None:
        nodeToRemove = node
        node = node.next
        if nodeToRemove.value == value:
            linkedList.remove(nodeToRemove)

def containsNodeWithValue(linkedList, value):
    node = linkedList.head
    while node is not None and node.value != value:
        node = node.next
    return node is not None

def remove(linkedList, node):
    if node == linkedList.head:
        linkedList.head = linkedList.head.next
    if node == linkedList.tail:
        linkedList.tail = linkedList.tail.prev
    removeNodeBindings(node)

def removeNodeBindings(node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.prev = None
    node.next = None

def insertBefore(linkedList, node, nodeToInsert):
    if nodeToInsert == linkedList.head and nodeToInsert == linkedList.tail:
        return
    linkedList.remove(nodeToInsert)
    nodeToInsert.prev = node.prev
    nodeToInsert.next = node
    if node.prev is None:
        linkedList.head = nodeToInsert
    else:
        node.prev.next = nodeToInsert
    node.prev = nodeToInsert

def insertAfter(linkedList, node, nodeToInsert):
    if nodeToInsert == linkedList.head and nodeToInsert == linkedList.tail:
        return
    linkedList.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    if node.next is None:
        linkedList.tail = nodeToInsert
    else:
        node.next.prev = nodeToInsert
    node.next = nodeToInsert


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = ProgrammingError.DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        three2 = Node(3)
        three3 = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        linkedList.setHead(one)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, one)
        linkedList.setTail(two)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, two)
        linkedList.insertAfter(one, two)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, two)
        self.assertEqual(one.next, two)
        self.assertEqual(two.prev, one)
        linkedList.insertAfter(two, three)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, two)
        self.assertEqual(two.prev, one)
        self.assertEqual(two.next, three)
        self.assertEqual(three.prev, two)
        linkedList.insertAfter(two, four)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, two)
        self.assertEqual(two.prev, one)
        self.assertEqual(two.next, four)
        self.assertEqual(four.prev, two)
        self.assertEqual(four.next, three)
        self.assertEqual(three.prev, four)
        linkedList.insertAfter(one, three2)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, three2)
        self.assertEqual(three2.prev, one)
        self.assertEqual(three2.next, two)
        self.assertEqual(two.prev, three2)
        self.assertEqual(two.next, four)
        self.assertEqual(four.prev, two)
        self.assertEqual(four.next, three)
        self.assertEqual(three.prev, four)
        linkedList.insertAfter(two, three3)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, three2)
        self.assertEqual(three2.prev, one)
        self.assertEqual(three2.next, two)
        self.assertEqual(two.prev, three2)
        self.assertEqual(two.next, three3)
        self.assertEqual(three3.prev, two)
        self.assertEqual(three3.next, four)
        self.assertEqual(four.prev, three3)
        self.assertEqual(four.next, three)
        self.assertEqual(three.prev, four)
        linkedList.insertAfter(one, five)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, five)
        self.assertEqual(five.prev, one)
        self.assertEqual(five.next, three2)
        self.assertEqual(three2.prev, five)
        self.assertEqual(three2.next, two)
        self.assertEqual(two.prev, three2)
        self.assertEqual(two.next, three3)
        self.assertEqual(three3.prev, two)
        self.assertEqual(three3.next, four)
        self.assertEqual(four.prev, three3)
        self.assertEqual(four.next, three)
        self.assertEqual(three.prev, four)
        linkedList.insertAfter(six, three)
        self.assertEqual(linkedList.head, one)
        self.assertEqual(linkedList.tail, three)
        self.assertEqual(one.next, five)
        self.assertEqual(five.prev, one)
        self.assertEqual(five.next, three2)
        self.assertEqual(three2.prev, five)
        self.assertEqual(three2.next, two)
        self.assertEqual(two.prev, three2)
        self.assertEqual(two.next, three3)
        self.assertEqual(three3.prev, two)
        self.assertEqual(three3.next, four)
        self.assertEqual(four.prev, three3)
        self.assertEqual(four.next, three)
        self.assertEqual(three.prev, four)
