"""
Write a function that takes in an array of integers and returns an array of length 2
representing the largest range of integers contained in that array.
The first number in the output array should be the first number in the range, while the
second number should be the last number in the range.
A range of numbers is defined as a set of numbers that come right after each other in the
set of real integers. For instance, the output array [2, 6] represents the range
{2, 3, 4, 5, 6} , which is a range of length 5. Note that numbers don't need to be
sorted or adjacent in the input array in order to form a range.
You can assume that there will only be one largest range.
Sample Input
array = [l, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6)

Sample Output
(0, 7)

"""

def largestRange(array):
    nums = set(array)
    maxLength = 0
    bestRange = []

    for num in nums:
        if num - 1 not in nums:
            currentLength = 1
            currentNum = num + 1

            while currentNum in nums:
                currentLength += 1
                currentNum += 1

            if currentLength > maxLength:
                maxLength = currentLength
                bestRange = [num, currentNum - 1]

    return bestRange
