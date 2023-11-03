"""
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0 s and 1 s. Each 0 represents land, and each 1 represents part of a river .. 0.. river consists of any number of 1 s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1 s forming a river determine its size. 
Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example. 
Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

Sample Input:

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

Sample Output:
    
    [1, 2, 2, 2, 5] # The numbers could be ordered differently.


"""

def riverSizes(matrix):
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 or matrix[i][j] == -1:
                continue
            size = checkLeftBottom(i, j, matrix)
            sizes.append(size)
    return sizes

def checkLeftBottom(i, j, matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0 or matrix[i][j] == -1:
        return 0
    matrix[i][j] = -1
    return 1 + checkLeftBottom(i - 1, j, matrix) + checkLeftBottom(i, j + 1, matrix) + checkLeftBottom(i + 1, j, matrix) + checkLeftBottom(i, j - 1, matrix)


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    print(riverSizes(matrix))

    