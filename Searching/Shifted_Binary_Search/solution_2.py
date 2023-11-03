"""
Write a function that takes 1n a sorted array of distinct integers as well as a target integer.
 The caveat is that the integers in the array have been shifted by some amount; 1n other words, 
 they've been moved to the left or to the right by one or more pos1t1ons. For example, [l, 2, 3, 4] might have turned into [3, 4, 1, 2] 
The function should use a variation of the Binary Search algorithm to determine 1f the target integer 1s contained 1n the array and should return its index if 1t is, 
otherwise -1 . If you·re unfamiliar with Binary Search, 
we recommend watching the Conceptual Overview section of the Binary Search question·s video explanation before starting to code. 

Sample Input
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33

Sample Output
8

Example Explanation
The target integer 33 1s located at 1ndex 8 1n the array.
This approach finds the correct indices of shifted sorted array and then applies naive bunary search. First , 
find the position of smallest element in shifted array which will be the number of steps the array has shifted. 
And then using modulas operator map "mid" to it's position in given shifted array. 

Time complexity: O(log(n)) 
Space complexity: 0(1) 

"""

def shiftedBinarySearch(array, target):
    # Write your code here.
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        potentialMatch = array[mid]
        leftNum = array[left]
        rightNum = array[right]
        if target == potentialMatch:
            return mid
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > potentialMatch and target <= rightNum:
                left = mid + 1
            else:
                right = mid - 1
    return -1

