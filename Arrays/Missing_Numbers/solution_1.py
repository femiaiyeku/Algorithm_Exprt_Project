
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
    includedNums = set(nums)

    solution = []
    for i in range(1, len(nums) + 3):
        if i not in includedNums:
            solution.append(i)

    return solution

# nums = [3, 1, 4]

# print(missingNumbers(nums))


# nums = [3, 1, 4]

# print(missingNumbers(nums))


# nums = [3, 1, 4]



