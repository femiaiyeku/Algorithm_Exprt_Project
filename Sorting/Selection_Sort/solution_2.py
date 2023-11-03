"""

Write a function that takes in an array of integers and returns a sorted version
that array. Use the Selection Sort algorithm to sort the array.
If you're unfamiliar with Selection Sort, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code.

Sample Input:
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output:
[2, 3, 5, 5, 6, 8, 9]



"""

def selectionSort(array):
    for i in range(len(array)):
       arg_min = min(range(i,len(array)), key=array.__getitem__)
       array[i], array[arg_min] = array[arg_min], array[i]
    return array


