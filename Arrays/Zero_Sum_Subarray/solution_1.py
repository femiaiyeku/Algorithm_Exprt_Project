"""
You're given a list of intergers nums.Write a function that returns a boolean representing wehether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray whose elements sum up to 0..A subarray is a contiguous part of an array.For the purpose of this question,
a subarray can be as small as one element and as long as the original array.


Sample Input
nums = [-5, -5. 2, 3, -2]

Sample Output
True // The subarray [-5, 2, 3] sums up to 0


"""

def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)

    return False



