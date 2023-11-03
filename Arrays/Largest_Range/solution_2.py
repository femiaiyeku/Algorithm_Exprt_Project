"""
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers contained 1n that array. 
The first number 1n the output array should be the first number 1n the range, while the second number should be the last number 1n the range. 
A range of numbers 1s defined as a set of numbers that come right after each other 1n the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6} , which is a range of length S. Note that numbers don't need to be sorted or adJacent 1n the input array 1n order to form a range. 
You can assume that there will only be one largest range. 
Sample Input
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample Output
[0, 7]


"""
# O(n) time | O(n) space

def largestRange(array):
    nums = set
    maxlength = 0 
    bestRange = []
    for num in array:
        nums.add(num)
    for num in array:
        if num not in nums:
            continue
        nums.remove(num)
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums.remove(left)
            currentLength += 1
            left -= 1
        while right in nums:
            nums.remove(right)
            currentLength += 1
            right += 1
        if currentLength > maxlength:
            maxlength = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange

