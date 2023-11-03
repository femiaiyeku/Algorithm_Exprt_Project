"""
You're given a list of intergers nums.Write a function that returns a boolean representing wehether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray whose elements sum up to 0..A subarray is a contiguous part of an array.For the purpose of this question,
a subarray can be as small as one element and as long as the original array.


Sample Input
nums = [-5, -5. 2, 3, -2]

Sample Output
True // The subarray [-5, 2, 3] sums up to 0


"""

#O(n) time | O(n) space - where n is the length of the input array

def zeroSumSubarray(nums):


    res = 0 
    sumMap = {0:1}
    currentSum = 0
    for num in nums:
        currentSum += num
        res += sumMap.get(currentSum, 0)
        sumMap[currentSum] = sumMap.get(currentSum, 0) + 1
        

    return res

print(zeroSumSubarray([-5, -5, 2, 3, -2])) # 3
print(zeroSumSubarray([0, 0, 0, 0, 0])) # 15
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1])) # 4
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0])) # 5
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0])) # 7
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0])) # 10
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0])) # 14
print(zeroSumSubarray([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0])) # 15
