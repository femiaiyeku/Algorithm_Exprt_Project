"""
You are given an array of points plotted on a 2D graph(the xy-plane). 
Write a function that returns the minimum area of any rectangle that can be formed using any 4 of these points such that the rectangle's sides are parallel to the x and y axes. 
If no rectangle can be formed, your function should return 0.

The input array will contain points represented by arrays of two integers [x, y].The input array will never contain duplicate points.

Sample Input:
points = [[1, 5], [-5, -1], [-1, -5], [5, 1]]

Sample Output:
12

Explanation:
The rectangle with corners [-5, -1], [-1, -5], [1, 5], and [5, 1], 
whose sides are parallel to the x and y axes, can be formed from these points,
 so your function should return 12.


"""

#O(n^2) time | O(n) space - where n is the number of points
def minimumAreaRectangle(points):
    columnns = initializeColumns(points)
    minAreaFound = float("inf")
    edgesParallelToAxes = {}
    for x in columnns:
        yIndices = columnns[x]
        yIndices.sort()
        for j in range(len(yIndices)):
            y2 = yIndices[j]
            for i in range(j):
                y1 = yIndices[i]
                pointString = str(y1) + "-" + str(y2)
                if pointString in edgesParallelToAxes:
                    x1 = edgesParallelToAxes[pointString]
                    area = abs(x - x1) * abs(y2 - y1)
                    minAreaFound = min(minAreaFound, area)
                edgesParallelToAxes[pointString] = x
    return minAreaFound if minAreaFound != float("inf") else 0

def initializeColumns(points):
    columns = {}
    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []
        columns[x].append(y)
    return columns

