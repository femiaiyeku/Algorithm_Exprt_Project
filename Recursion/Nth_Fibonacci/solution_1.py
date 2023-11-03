"""
The Fibonacci sequence is defined 35 follows: the first number of the sequence is 0 , the second number is 1 , 
and the nth number is the sum of the (n - 1 )th and {n - 2)th numbers. 
Write a function that takes in an integer n and returns the nth Fibonacci number. 
Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and Fl = 1 . 
For the purpose of this question, 
the first Fibonacci number is F0; therefore, getNthFib(l) is equal to F0, getNthFib(2) is equal to Fl, etc.. 

Sample input #1: 2
Sample output #1: 1 (0, 1)

Sample input #2: 6
Sample output #2: 5 (0, 1, 1, 2, 3, 5)

Sample input #3: 8

Sample output #3: 13 (0, 1, 1, 2, 3, 5, 8, 13)


"""


# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

    

