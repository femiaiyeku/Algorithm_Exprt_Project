"""
Write a function that takes in a non-ernpty array of distinct integers and an integer
representing a target surn. If any two nurnbers in the input array surn up to the target surn,
the function should return thern in an array, in any order. If no two nurnbers surn up to the
target surn, the function should return an ernpty array.
Note that the target sum has to be obtained by summing two different integers in the
array; you can't add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of nurnbers summing up to the target
sum

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10)
sequence = [l, 6, -1, 10)

Sample Output

true

"""


# Time: O(n) | Space: O(n)

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
