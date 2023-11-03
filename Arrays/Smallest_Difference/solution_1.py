"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position. 
Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1. 
You can assume that there will only be one pair of numbers with the smallest difference. 

Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output
[28, 26]


"""

#O(nlog(n) + mlog(m)) time | O(1) space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firsrtNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firsrtNum < secondNum:
            current = secondNum - firsrtNum
            idxOne += 1
        elif secondNum < firsrtNum:
            current = firsrtNum - secondNum
            idxTwo += 1
        else:
            return [firsrtNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firsrtNum, secondNum]
    return smallestPair

