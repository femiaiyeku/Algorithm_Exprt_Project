"""
Write a MinMaxStack class for a Min Max Stack. The class should support: 

• 	Pushing and popping values on and off the stack. 
• 	Peeking at the value at the top of the stack.
• 	Getting both the minimum and the maximum values in the stack at any given point in time.

All class methods, when considered independently, should run in constant time and with constant space. 


Sample Usuage

M1nMaxStack(): -push(S): -getM1 n(): 5 getMax(): 5 peek(): 5 



"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        minMaxStack = ProgrammingError.MinMaxStack()
        minMaxStack.push(5)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(7)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 7)
        self.assertEqual(minMaxStack.peek(), 7)
        minMaxStack.push(2)
        self.assertEqual(minMaxStack.getMin(), 2)
        self.assertEqual(minMaxStack.getMax(), 7)
        self.assertEqual(minMaxStack.peek(), 2)
        self.assertEqual(minMaxStack.pop(), 2)
        self.assertEqual(minMaxStack.pop(), 7)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        self.assertEqual(minMaxStack.pop(), 5)
        self.assertEqual(minMaxStack.getMin(), None)
        self.assertEqual(minMaxStack.getMax(), None)
        self.assertEqual(minMaxStack.peek(), None)
        minMaxStack.push(5)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(7)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 7)
        self.assertEqual(minMaxStack.peek(), 7)
        minMaxStack.push(2)
        self.assertEqual(minMaxStack.getMin(), 2)
        self.assertEqual(minMaxStack.getMax(), 7)
        self.assertEqual(minMaxStack.peek(), 2)
        self.assertEqual(minMaxStack.pop(), 2)
        self.assertEqual(minMaxStack.pop(), 7)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        self.assertEqual(minMaxStack.pop(), 5)
        self.assertEqual(minMaxStack.getMin(), None)
        self.assertEqual(minMaxStack.getMax(), None)
        self.assertEqual(minMaxStack.peek(), None)
        minMaxStack.push(5)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(5)
        self.assertEqual
        (minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(5)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 5)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(8)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 8)
        self.assertEqual(minMaxStack.peek(), 8)
        minMaxStack.push(8)
        self.assertEqual(minMaxStack.getMin(), 5)
        self.assertEqual(minMaxStack.getMax(), 8)
        self.assertEqual(minMaxStack.peek(), 8)
        minMaxStack.push(0)
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 8)
        self.assertEqual(minMaxStack.peek(), 0)
        minMaxStack.push(8)
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 8)
        self.assertEqual(minMaxStack.peek(), 8)
        minMaxStack.push(9)
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 9)
        self.assertEqual(minMaxStack.peek(), 9)
        minMaxStack.push(5)
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 9)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.push(1)
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 9)
        self.assertEqual(minMaxStack.peek(), 1)
        minMaxStack.pop()
        minMaxStack.pop()
        self.assertEqual(minMaxStack.getMin(), 0)
        self.assertEqual(minMaxStack.getMax(), 9)
        self.assertEqual(minMaxStack.peek(), 5)
        minMaxStack.pop()



