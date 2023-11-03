"""
You re given an array of integers and an integer .
Write a function that moves all instances of that integer 1n the array to the end of the array and returns the array The function should perform this in place (1 e, 
1t should mutate the input array) and doesn t need to maintain the order of the other integers 

Sample Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]

Sample Output:
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

"""

# Time Complexity: O(n) 

def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 1
    j = len(array) - 1
    while i < j:
        if array[i] == toMove:
            while array[j] == toMove:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        i += 1
    return array

