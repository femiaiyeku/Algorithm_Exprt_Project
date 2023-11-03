"""

Write a function that takes in an array of at least three integers and, 
without sorting the input array, returns a sorted array of the three largest integers 1n the input array. 
The function should return duplicate integers 1f necessary; for example, 1t should return [10, 18, 12] for an input array of 

[10, 5, 9, 10,12]

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output:
[18, 141, 541]


"""

#o(w + h) time | O(1) space
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
            sums[row][col] = sums[row - 1][col] + \
                sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
    return sums

