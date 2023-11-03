"""
You're given a two-dimensional ar·ay (a matrix) of potentially unequal height and width containing only 0 sand 1 s. 
The matrix represents a two-toned image, where each 1 represents black and each 0 represents white.
 An island is defined as any number of 1 s that are horizonta ly or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of 1orizontally or vertically adjacent 1 s isn't an island if any of those 1 s are in the first row, last row, first column, or last column of the input matrix. 
Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L­shaped, for example. 
You can think of islands as patches of black that don't touch the border of the two-toned image. 
Write a function that returns a modified version of the input matrix, where all of the islands are removed. You remove an island by replacing it with 0 s. 
Naturally, you're allowed to mutate the input matrix. 


Sample Input:

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
    ]


Sample Output:

[
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
]



// The islands that were removed can be clearly seen here:

[
    [ ,  ,  ,  ,  ,  ],
    [ , 1,  ,  ,  ,  ],
    [ ,  , 1,  ,  ,  ],
    [ ,  ,  ,  ,  ,  ],
    [ ,  , 1, 1,  ,  ],
    [ ,  ,  ,  ,  ,  ],
]


// There are other valid solutions, too.




"""
#O(wh) time | O(wh) space - where w and h are the width and height of the input matrix
# arc the width and height of the input matrix


def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]:
                continue

            matrix[row][col] = 0

    return matrix


def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
        if alreadyVisited:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    if row + 1 < numRows:
        neighbors.append((row + 1, col))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < numCols:
        neighbors.append((row, col + 1))

    return neighbors


