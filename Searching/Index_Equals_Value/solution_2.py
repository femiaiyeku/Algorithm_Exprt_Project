"""

Write a function that takes in a saned array of distinct integers and returns the first index in the array that is equal to the value at
that index. In other words, your function should return the minimum index where index == array[index].
if there is no such index, your function should return -1.

Sample Input:

array = [-5, -3, 0, 3, 4, 5, 9]

Sample Output:

3

"""


# Solution 1: Iterative Solution with Linear Time Complexity    O(n) time | O(1) space
#####################################################################################

def indexEqualsValue(array):
    if not array:
        return -1
    

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < mid:
            low = mid + 1
        elif array[mid] == mid and mid == 0:
            return mid
        elif array[mid] == mid and array[mid - 1] < mid - 1:
            return mid
        else:
            high = mid - 1

    return -1

