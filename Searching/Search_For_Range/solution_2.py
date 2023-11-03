"""
Write a function that takes in a sorted array of integers as well as a target integer. 
The function should use a variation of the Binary Search algorithm to find a range of indices in between 
which the target number 1s contained 1n the array and should return this range in the form of an array 
The first number 1n the output array should represent the first index at which the target number 1s located, 
while the second number should represent the last index at which the target number 1s located The function 
should return [-1, -1] if the integer isn't contained in the array 
If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary 
Search question's video explanation before starting to code. 

Sample Input:
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45


Sample Output:
[4, 9]

"""

def searchForRange(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1

    resRange = [-1, -1]


    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

        else:
            resRange = [mid, mid]
            break

    if resRange[0] != -1:
        left = mid - 1
        while left >= 0 and array[left] == target:
            resRange[0] = left
            left -= 1

        right = mid + 1
        while right < len(array) and array[right] == target:
            resRange[1] = right
            right += 1

    return resRange

print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary
# Search question's video explanation before starting to code.
#   leftIdx = alteredBinarySearch(array, target, 0, len(array) - 1, True)
#   if leftIdx == -1:
#       return [-1, -1]
#   rightIdx = alteredBinarySearch(array, target, leftIdx, len(array) - 1, False)
#   return [leftIdx, rightIdx]
#
