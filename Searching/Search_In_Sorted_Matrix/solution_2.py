"""
You're given a two-dimensional array (a matrix) of distinct integers and a target integer. 
Each row in the matrix is sorted, and each column is also sorted; 
the matrix doesn't necessarily have the same height and width. 
Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise

If the target integer is not contained in the matrix, your function should return [-1, -1].

Sample Input

matrix = [
[1, 4, 7, 12, 15, 1000],
[2, 5, 19, 31, 32, 1001],
[3, 8, 24, 33, 35, 1002],
[40, 41, 42, 44, 45, 1003],
[99, 100, 103, 106, 128, 1004],
]

target = 44

Sample Output

[3, 3]


"""


# O(n + m) time | O(1) space

def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return [i, j]
    return [-1, -1]

