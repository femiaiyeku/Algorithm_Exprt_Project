"""
You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.
The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-
left to bottom-right); it switches the row and column indices of the original matrix.
You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the
same.


Sample Input
matrix = [
[1, 2],
]

Sample Output
[
[1],
[2],
]





"""

def transposeMatrix(matrix):
    # Write your code here
    transposeMatrix = []
    for col in range(len(matrix[0])):
        transposeMatrix.append([])
        for row in range(len(matrix)):
            transposeMatrix[col].append(matrix[row][col])
    return transposeMatrix

