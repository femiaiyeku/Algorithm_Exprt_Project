"""
Write a MinMaxStack class for a Min Max Stack. The class should support: 

• 	Pushing and popping values on and off the stack. 
• 	Peeking at the value at the top of the stack.
• 	Getting both the minimum and the maximum values in the stack at any given point in time.

All class methods, when considered independently, should run in constant time and with constant space. 


Sample Usuage

M1nMaxStack(): -push(5): -getM1 n(): 5 getMax(): 5 peek(): 5
-push(7): -getM1 n(): 5 getMax(): 7 peek(): 7
-push(2): -getM1 n(): 2 getMax(): 7 peek(): 2
-pop(): -pop(): -getM1 n(): 5 getMax(): 5 peek(): 5




"""

import collections


class MinMaxStack:
    def __init__(self):
        self.maxes = []
        self.mins = []
        self.storage = []

    def peek(self):
        return self.storage[-1] if self.storage else None
    
    def pop(self):
        if self.storage:
            self.maxes.pop()
            self.mins.pop()
            return self.storage.pop()
        else:
            return None
        
    def push(self, number):
        self.storage.append(number)
        if self.maxes:
            self.maxes.append(max(number, self.maxes[-1]))
            self.mins.append(min(number, self.mins[-1]))
        else:
            self.maxes.append(number)
            self.mins.append(number)

    def getMin(self):
        return self.mins[-1] if self.mins else None
    
    def getMax(self):
        return self.maxes[-1] if self.maxes else None
    
