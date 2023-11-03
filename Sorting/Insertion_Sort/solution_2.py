"""
Write a function that takes in an array of integers and returns a sorted version of
that array. Use the Insertion Sort algorithm to sort the array.
If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code

Sample Input:
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output:
[2, 3, 5, 5, 6, 8, 9]


"""

def insertionSort(array):
    for idx in range(len(array)):
        while idx > 0 and array[idx] < array[idx-1]:
            swap(idx, idx-1, array)
            idx -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

    