"""
Write a MinMaxStack class for a Min Max Stack. The class should support: 

• 	Pushing and popping values on and off the stack. 
• 	Peeking at the value at the top of the stack.
• 	Getting both the minimum and the maximum values in the stack at any given point in time.

All class methods, when considered independently, should run in constant time and with constant space. 


Sample Usuage

M1nMaxStack(): -push(S): -getM1 n(): 5 getMax(): 5 peek(): 5 



"""

#O(1) time | O(1) space

class MinMaxStack:
    def __init__(self) -> None:
        self.minMaxStack = []
        self.stack = []

        def peek(self):
            return self.stack[len(self.stack) - 1]
        

        def pop(self):
            self.minMaxStack.pop()
            return self.stack.pop()
        

        def push(self, number):
            newMinMax = {"min": number, "max": number}
            if len(self.minMaxStack):
                lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
                newMinMax["min"] = min(lastMinMax["min"], number)
                newMinMax["max"] = max(lastMinMax["max"], number)
            self.minMaxStack.append(newMinMax)
            self.stack.append(number)



        def getMin(self):
            return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
        

        def getMax(self):
            return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
        
    

    


