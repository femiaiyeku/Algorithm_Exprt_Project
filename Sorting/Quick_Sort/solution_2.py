"""
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Quick Sort algorithm to sort the array.  If you're unfamiliar with Quick Sort, 
we recommend watching the Conceptual Overview section of this question's video explanation before starting to code. 

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]


"""

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quickSort(less) + [pivot] + quickSort(greater)
    pass
    
print(quickSort([8, 5, 2, 9, 5, 6, 3]))
print(quickSort([8, 5, 2, 9, 5, 6, 3, 1, 4, 7, 0]))
print(quickSort([8, 5, 2, 9, 5, 6, 3, 1, 4, 7, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
print(quickSort([8, 5, 2, 9, 5, 6, 3, 1, 4, 7, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, -1, -2, -3, -4, -5, -6, -7, -8, -9]))

