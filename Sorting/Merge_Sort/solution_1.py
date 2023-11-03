"""
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Merge Sort algorithm to sort the array. 
If you're unfamiliar with Merge Sort,
 we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output

[2, 3, 5, 5, 6, 8, 9]

"""
#O(nlog(n)) time | O(nlog(n)) space


def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray

