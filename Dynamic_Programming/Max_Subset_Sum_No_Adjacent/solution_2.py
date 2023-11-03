"""

Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array. If the input array is empty, 
the function should return e . 

Sample Input: array = [75, 105, 120, 75, 90, 135]

Sample Output: 330 // 75 + 120 + 135





"""


def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0, 0
    for num in array:
        temp = currentMax
        currentMax = max(previousMax + num, currentMax)
        previousMax = temp


    return currentMax
