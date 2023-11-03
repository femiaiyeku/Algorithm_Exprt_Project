"""
Largest Island
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only es and 1 s.
Each 1 represents water, and each represents part of a land mass. A land mass consists of any number of es
that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacentes forming a
land mass determine its size.
Note that a land mass can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
it can be L-shaped, for example.
Write a function that returns the largest possible land mass size after changing exactly one 1 to a
given matrix will always contain at least one 1, and you may mutate the matrix.

Sample Input
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

Sample Output
6
// The 1 at row index 0 and column index 2 can be changed to a 1 to connect to the other 1s and form a land mass of size 6:

// [
    '1', 0, '0', 1, 0,
    '1', 0, '1', 0, 0,
    '0', 0, '1', 0, 1,
    '1', 0, '1', 0, 1,
    '1', 0, '1', '1', 0,
]
"""

def largestIsland(matrix):
    maxSize = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                size = dfs(matrix, i, j)
                maxSize = max(maxSize, size)

    return maxSize
 

def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
        return 0

    matrix[i][j] = 2
    size = 1
    size += dfs(matrix, i+1, j)
    size += dfs(matrix, i-1, j)
    size += dfs(matrix, i, j+1)
    size += dfs(matrix, i, j-1)

    return size

# Time: O(n*m)
# Space: O(n*m)
