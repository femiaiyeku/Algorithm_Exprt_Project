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

def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    ans = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1

    return ans

#O(nlog(n)) time | O(nlog(n)) space


