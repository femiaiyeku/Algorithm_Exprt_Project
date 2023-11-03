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

#O(n^2) time | O(n) space   where n is the number of points
def countSquares(points):
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

        return count
    
def pointToString(point):
    return str(point[0]) + "-" + str(point[1])



