"""

You're given an unordered list of unique integers nums in the range [1, n] , where n represents the length of nums + 2 . This means that two numbers in this range are missing from the list. 
Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically. 

Example:
Input:
nums = [3, 1, 4]
Output:
[2, 5]



"""



def missingNumbers(nums):
    # Write your code here
    nums.sort()
    n = len(nums)
    res = []
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 1:
            res.append(nums[i] - 1)
    return res

