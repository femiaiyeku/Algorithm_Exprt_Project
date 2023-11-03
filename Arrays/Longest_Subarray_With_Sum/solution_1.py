"""
Write a function that takes in a non-empty array of non-negative integers and a non-negative integer representing a target sum.The function should find the 
longest subarray where the values collectively sum up to equal the target  sum. Return an array containing the starting index and ending index of this subarray both inclusive.
If there is no subarray that sums up top the target sunm, the function should return an empty array. You can assume that the given inputs will only ever have one answer.

Sample Input:
array = [1,2,3,4,3,3,1,2,1,2]

targetSum = 10


Sample Output:

[4, 8] // The longest subarray that sums to 10 starts at index 4 and ends at index 8.

"""

def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    indices = []
    for startingIndex in range(len(array)):
        for endingIndex in range(startingIndex, len(array)):
            if sum(array[startingIndex:endingIndex + 1]) == targetSum:
                indices.append([startingIndex, endingIndex])
    if len(indices) == 0:
        return []
    else:
        return indices[0]
    
    