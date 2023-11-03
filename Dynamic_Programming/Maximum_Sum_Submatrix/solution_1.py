"""

You're given a two-dimensional array (a matrix) of potentially unequal height and width that's filled with integers. 
You're also given a positive integer size . Write a function that returns the maximum sum that can be generated from a sub matrix with dimensions size * size , 
For example, consider the following matrix: 


[
    [2, 4],
    [5, 6],
    [-3, 2],
]

If size = 2 , then the 2x2 sub matrices to consider are:

[
    [2, 4],
    [5, 6],
]

[
    [5, 6],
    [-3, 2],
]

The sum of the elements in the first sub matrix is 17 , and the sum of the elements in the second sub matrix is 10 .
In this example, your function should return 17 .

Note: You can assume that size is less than or equal to the height and width of the input matrix.

Sample Input

matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2],
]

size = 2


Sample Output

18


"""

# Solution 1: Brute Force
#O(W * h * size^2) time | O(1) space - where W and H are the width and height of the input matrix

def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]

            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]

            maxSubMatrixSum = max(maxSubMatrixSum, total)

    return maxSubMatrixSum

def createSumMatrix(matrix):
    sums = [[0 for col in range(len(matrix[row]))] for row in range(len(matrix))]

    sums[0][0] = matrix[0][0]

    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]

    return sums


