"""
You're given two positive integers representing the width and height of a grid-shaped, rectangular graph. Write a
function that returns the number of ways to reach the bottom right corner of the graph when starting at the top left
corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.
3, there are three ways to reach the
For example, given the graph illustrated below, with width 2 and height
bottom right corner when starting at the top left corner.

1 2
3 4
5 6

1. Down, Down, Right
2. Right, Down, Down
3. Down, Right, Down

Note: you may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.



Sample Input
width = 4
height = 3

Sample Output

10



"""


def numberOfWaysToTraverseGraph(width, height):
    ways = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                ways[heightIdx][widthIdx] = 1
            else:
                ways[heightIdx][widthIdx] = ways[heightIdx - 1][widthIdx] + ways[heightIdx][widthIdx - 1]
    return ways[height][width]

