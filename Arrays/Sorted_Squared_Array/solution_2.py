"""
Write a function that takes 1n a non empty array of integers that are sorted 1n ascending order and 
returns a new array of the same length with the squares of the original integers also sorted 1n ascending order 

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output

[1, 4, 9, 25, 36, 64, 81]



"""

# Time Complexity: O(n)
# Space Complexity: O(n)

def sortedSquaredArray(array):
    out = [0] * len(array)
    mint = 0
    maxt = len(array) - 1
    for idx in reversed(range(len(array))):
        if abs(array[mint]) > abs(array[maxt]):
            out[idx] = array[mint] * array[mint]
            mint += 1
        else:
            out[idx] = array[maxt] * array[maxt]
            maxt -= 1
    return out

