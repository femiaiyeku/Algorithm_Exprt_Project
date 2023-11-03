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
    visited = set()
    min_area = float("inf")
    
    for x1, y1 in points:
        for x2, y2 in visited:
            if (x1, y2) in visited and (x2, y1) in visited:
                area = abs(x1 - x2) * abs(y1 - y2)
                min_area = min(min_area, area)
        visited.add((x1, y1))

    return min_area if min_area != float("inf") else 0

