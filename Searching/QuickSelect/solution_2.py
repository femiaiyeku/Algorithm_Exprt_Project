"""
Write a function that takes in an array of distinct Integers as well as an integer k
and that returns the kth smallest integer in that array.
The function should do this in linear time, on average.

Sample Input
array = [8, 5, 2, 9, 7, 6, 3]

k=3

Sample Output
5

"""

def quickselect(array, k):
   left = 0
   right = len(array) - 1
   while left <=right:
        pivot = partition(array, left, right)
        if pivot == k - 1:
            return array[pivot]
        elif pivot < k - 1:
            left = pivot + 1
        else:
            right = pivot - 1
            return -1

def partition(array, left, right):
    pivot = array[left]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            swap(left, right, array)
            left += 1
            right -= 1
    return left

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


        