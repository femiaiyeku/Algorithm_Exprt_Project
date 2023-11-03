"""
A city wants to build a new public park, and you've been tasked with finding the largest park they can build without
disturbing existing infrastructure.
Write a function that takes in a two-dimensional array (a matrix) Land representing the total land of the city from
a top-down view. Each value in land is a boolean; false values are pleces of land not currently in use, while true
values are pleces of land currently in use by other infrastructure. Return the area of the largest possible park.
The largest possible park will be placed exclusively on unused land (false values). Moreover, the city wants the
park to be a perfect rectangle. If there is no available land, your function should return 0.
Note that you're always given at least one piece of land to use (there will always be at least one true value in land).
Also note that you can't place a park on the edges of the city, since that would require extending the park beyond
the boundaries of the city.
Sample Input
land = [
[false, true, true, false],
[false, false, true, false],
[true, true, false, true],
[false, false, true, false],
]
Sample Output
6

// The park should be made up of the land at row indices 1-2 and column indices 2-3, as follows:
// [
// [false, true, true, false],
// [false, false, true, false],
// [true, true, false, true],
// [false, false, true, false],
// ]
// The area of this park is 2 * 3 = 6.


"""
#O(w*h) time | O(w*h) space - where w and h are the width and height of the input matrix


def largestPark(land):
    heights = [0] * len
    maxArea = 0

    for row in land:
        for col in range(len(row)):
            if row[col]:
                heights[col] += 1
            else:
                heights[col] = 0

    return maxArea



def largestRectangleHistogram(heights):
    stack = []
    maxArea = 0


    for columnIndex in range(len(heights)):
        while len(stack) > 0 and heights[stack[len(stack) - 1]] >= heights[columnIndex]:
            pillarIndex = stack.pop()
            width = columnIndex - stack[len(stack) - 1] - 1 if len(stack) > 0 else columnIndex
            maxArea = max(maxArea, heights[pillarIndex] * width)
        stack.append(columnIndex)

    while len(stack) > 0:
        pillarIndex = stack.pop()
        width = len(heights) - stack[len(stack) - 1] - 1 if len(stack) > 0 else len(heights)
        maxArea = max(maxArea, heights[pillarIndex] * width)

    return maxArea



