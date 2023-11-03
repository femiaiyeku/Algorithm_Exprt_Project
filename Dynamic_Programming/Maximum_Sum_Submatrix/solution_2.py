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

#O(W * h * size^2) time | O(1) space - where W and H are the width and height of the input matrix

def maximumSumSubmatrix(matrix, size):
    maxSum = float("-inf")
    sums = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            sums[row][col] = matrix[row][col]
            if row > 0:
                sums[row][col] += sums[row - 1][col]
            if col > 0:
                sums[row][col] += sums[row][col - 1]
            if row > 0 and col > 0:
                sums[row][col] -= sums[row - 1][col - 1]
            rowStart = row - size

            colStart = col - size
            if rowStart >= 0 and colStart >= 0:
                total = sums[row][col]
                if colStart >= 0:
                    total -= sums[row][colStart]
                if rowStart >= 0:
                    total -= sums[rowStart][col]
                if rowStart >= 0 and colStart >= 0:
                    total += sums[rowStart][colStart]
                maxSum = max(maxSum, total)

    return maxSum

def main():
    matrix = [
        [5, 3, -1, 5],
        [-7, 3, 7, 4],
        [12, 8, 0, 0],
        [1, -8, -8, 2],
    ]

    size = 2

    print(maximumSumSubmatrix(matrix, size))

main()


