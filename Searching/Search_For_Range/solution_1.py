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
    finalRange = [-1, -1]
    alterBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alterBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange

def alterBinarySearch(array, target, left, right, finalRange, goLeft):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        alterBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
    elif array[mid] > target:
        alterBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                alterBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                alterBinarySearch(array, target, mid + 1, right, finalRange, goLeft)

print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary
# Search question's video explanation before starting to code.
#   leftIdx = alteredBinarySearch(array, target, 0, len(array) - 1, True)
#   if leftIdx == -1:
#       return [-1, -1]
#   rightIdx = alteredBinarySearch(array, target, leftIdx, len(array) - 1, False)

           


