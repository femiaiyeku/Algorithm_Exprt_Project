"""

Write a function that takes in a square-shaped n x n two-dimensional array of only 1 s and Os and returns a boolean representing 
whether the input matrix contains a square whose borders are made up of only Os. 
Note that a 1 x 1 square doesn't count as a valid square for the purpose of this question.
 In other words, a singular e in the input matrix doesn't constitute a square whose borders are made up of only Os; a square of zeroes has to be at least 2 x 2. 


Sample Input:
matrix = [
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

Sample Output:

true



"""


#O(n^3) time | O(n^2) space - where n is the height and width of the matrix

def squaresOfZeroes(matrix):
    lastIdx = len(matrix) - 1
    for topRow in range(len(matrix)):
        for leftCol in range(len(matrix)):
            squareLength = 2
            while squareLength <= len(matrix) - topRow and squareLength <= len(matrix) - leftCol:
                bottomRow = topRow + squareLength - 1
                rightCol = leftCol + squareLength - 1
                if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
                    return True
                squareLength += 1
    return False

def isSquareOfZeroes(matrix, r1, c1, r2, c2):
    for row in range(r1, r2 + 1):
        if matrix[row][c1] != 0 or matrix[row][c2] != 0:
            return False
    for col in range(c1, c2 + 1):
        if matrix[r1][col] != 0 or matrix[r2][col] != 0:
            return False
    return True

