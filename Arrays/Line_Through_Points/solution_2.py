"""
You·re given an array of po,nts plotted on a 2D graph (the xy-plane). 
Write a function that returns the maximum number of points that a single line (or potentially multiple lines) on the graph passes through. 
The ,nput array will contain points represented by an array of two integers [x, y] .
 The input array will never contain duplicate points and will always contain at least one point. 

Sample Input
points = [
[-1, 0],
[0, 0],
[1, 0],
[2, 0],
[3, 0],
[3, 1],
]

Sample Output
4 // A line passes through points [-1, 0], [0, 0], [1, 0], [2, 0]



"""

def lineThroughPoints(points):
    res = 1
    for i in range(len(points)):
        p1 = points[i]
        count = dict()
        for j in range(i+1, len(points)):
            p2 = points[j]
            slope = getSlope(p1, p2)
            if slope not in count:
                count[slope] = 0
            count[slope] += 1
        res = max(res, max(count.values())+1)
    return res

def getSlope(p1, p2):
    if p1[0] == p2[0]:
        return float("inf")
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def getSlopeOfLineBetweenPoints(p1, p2):
    if p1[0] == p2[0]:
        return float("inf")
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def isEquivalentSlope(slope1, slope2):
    return abs(slope1 - slope2) < 0.0001

def isPointOnLine(point, pointOnLine, slope):
    if point[0] == pointOnLine[0] and point[1] == pointOnLine[1]:
        return True
    if slope == float("inf"):
        return pointOnLine[0] == point[0]
    return isEquivalentSlope(getSlope(pointOnLine, point), slope)

def updateLineThroughPoint(point, slope, lineThroughPoint):
    if lineThroughPoint["slope"] == slope:
        lineThroughPoint["count"] += 1
    else:
        lineThroughPoint["count"] = 2
        lineThroughPoint["slope"] = slope
    return lineThroughPoint

def lineThroughPoints(points):
    if len(points) <= 2:
        return len(points)
    maxNumberofPointsOnLine = 1
    for idx1, p1 in enumerate(points):
        slopes = {}
        for idx2, p2 in enumerate(points):
            if idx1 == idx2:
                continue
            slope = getSlope(p1, p2)
            if slope not in slopes:
                slopes[slope] = 1
            slopes[slope] += 1
        currentMax = max(slopes.values())
        maxNumberofPointsOnLine = max(maxNumberofPointsOnLine, currentMax)
    return maxNumberofPointsOnLine
