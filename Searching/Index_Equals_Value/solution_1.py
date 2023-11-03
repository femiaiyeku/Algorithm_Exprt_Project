"""

Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the value at
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
    for index, value in enumerate(array):
        if index == value:
            return index
    return -1
