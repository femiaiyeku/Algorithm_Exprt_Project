"""
Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all of
those arrays.
The integers in the merged list should be in sorted order.

Sample Input:
arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]
]

Sample Output:
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]


"""

def mergeSortedArrays(arrays):
    result = arrays[0]
    for i in range(1, len(arrays)):
        result = mergeTwoSortedArrays(result, arrays[i])

    return result

def mergeTwoSortedArrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


