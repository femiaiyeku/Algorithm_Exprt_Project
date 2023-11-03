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

def getSlopeOfLineBetweenPoints(p1, p2):
    if p1[0] == p2[0]:
        return float("inf")
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def getSlope(p1, p2):
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
        lineThroughPoint["slope"] = slope
        lineThroughPoint["count"] = 2

def lineThroughPoints(points):
    if len(points) <= 2:
        return len(points)
    maxNumberofPointsOnLine = 1
    for p1 in points:
        slopes = {}
        for p2 in points:
            if p1 == p2:
                continue
            slope = getSlopeOfLineBetweenPoints(p1, p2)
            if slope not in slopes:
                slopes[slope] = {"count": 1, "point": p1}
            updateLineThroughPoint(p2, slope, slopes[slope])
            maxNumberofPointsOnLine = max(maxNumberofPointsOnLine, slopes[slope]["count"])
    return maxNumberofPointsOnLine



