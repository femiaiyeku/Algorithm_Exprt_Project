"""
Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and 
returns the number of squares that can be formed by these coordinates. 
A square must have its four corners amongst the coordinates in order to be counted. 
A single coordinate can be used as a corner for multiple different squares. 
You can also assume that no coordinate will be farther than 100 units from the origin. 

Sample Input

points = [
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (4, 3),
]

Sample Output

8   // The 8 squares are:
    // 1: (1, 1), (1, 2), (2, 1), (2, 2)
    // 2: (1, 2), (1, 3), (2, 2), (2, 3)
    // 3: (2, 1), (2, 2), (3, 1), (3, 2)
    // 4: (2, 2), (2, 3), (3, 2), (3, 3)
    // 5: (1, 1), (1, 2), (1, 3), (2, 3)
    // 6: (1, 2), (1, 3), (1, 4), (2, 4)
    // 7: (2, 1), (2, 2), (2, 3), (3, 3)
    // 8: (2, 2), (2, 3), (2, 4), (3, 4)
    


"""
import math
#O(n^2) time | O(n) space   where n is the number of points

def countSquares(points):
    def matrix_action(matrix, vector):
        return [sum([a * b for a, b in zip(row, vector)]) for row in matrix]

    def matrix_multiplication(matrixA, matrixB):
        return [matrix_action(matrixA, col) for col in zip(*matrixB)]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 1:
            return matrix_multiplication(matrix, matrix_power(matrix, power - 1))
        else:
            matrixA = matrix_power(matrix, power / 2)
            return matrix_multiplication(matrixA, matrixA)
        
    def pointToString(point):
        return str(point[0]) + '-' + str(point[1])

    pointsSet = set()
    for point in points:
        pointsSet.add(pointToString(point))

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midpoint = [(pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2]
            xDistance = abs(pointA[0] - pointB[0]) / 2
            yDistance = abs(pointA[1] - pointB[1]) / 2
            pointC = [midpoint[0] + yDistance, midpoint[1] - xDistance]
            pointD = [midpoint[0] - yDistance, midpoint[1] + xDistance]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                count += 1

    matrix = [[1, 1, 0], [-1, 1, 0], [0, 0, 1]]
    matrixToThePowerOfN = matrix_power(matrix, 100)
    vector = [0, 0, 1]
    for point in points:
        vector[0] = point[0]
        vector[1] = point[1]
        vector = matrix_action(matrixToThePowerOfN, vector)
        count += math.floor(vector[0] / 2) + math.floor(vector[1] / 2)

    return count
