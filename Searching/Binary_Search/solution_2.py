"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search
algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

Sample Input:

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

target = 33

Sample Output:
3

"""




# O(log(n)) time | O(1) space

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1




