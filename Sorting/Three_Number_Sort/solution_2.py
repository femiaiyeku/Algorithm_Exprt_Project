"""
You're given an array of Integers and another array of three distinct Integers. The first array is guaranteed
only contain Integers that are in the second array, and the second array represents a desired order for the
integers in the first array. For example, a second array of [x, y, z1 represents a desired order of
[X, X, X, Y YY, 2, 2, 2] In the first array.
Write a function that sorts the first array according to the desired order in the second array.
The function should perform this in place (i.e., It should mutate the input array), and it shouldn't use any
auxiliary space (1.e., it should run with constant space: 0(1) space).
Note that the desired order won't necessarily be ascending or descending and that the first array won't
necessarily contain all three integers found in the second array-It might only contain one or two.

Sample Input
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

Sample Output
[0, 0, 0, 1, 1, 1, -1, -1]

"""

def threeNumberSort(array, order):
    index = 0
    for i in range(2):
        val = order[i]
        for j in range(len(array)):
            if array[j] == val:
                array[index], array[j] = array[j], array[index]
                index += 1


    return array

# O(n) time | O(1) space - where n is the length of the array
