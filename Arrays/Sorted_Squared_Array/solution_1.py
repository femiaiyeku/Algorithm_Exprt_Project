"""
Write a function that takes 1n a non empty array of integers that are sorted 1n ascending order and 
returns a new array of the same length with the squares of the original integers also sorted 1n ascending order 

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output

[1, 4, 9, 25, 36, 64, 81]



"""
# Time Complexity: O(nlog(n))

# Space Complexity: O(n)

def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value
    sortedSquares.sort()
    return sortedSquares



