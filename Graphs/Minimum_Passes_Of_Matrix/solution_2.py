"""
Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of passes required to convert all negative integers
 in the matrix to positive integers. 
A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements is positive.
An adjacent element is an element thct is to the left, to the right, above, or below the current element in the matrix. 
Converting a negative to a positive simply involves multiplying it by -1 
Note that the 0 value is neither p3sitive nor negative, meaning that a 0 can't convert an adjacent negative to a positive. 
A single pass through the matrix in􀀟olves converting all the negative integers that can be converted at a particular point in time. 
For example, consider the following input matrix: 

[

[0, -2, -1],
    
    [-5, 2, 0],
    
    [-6, -2, 0]
    
    ]

After a first pass, only 3 values can be converted to positives:

[

[0, 2, -1],

[5, 2, 0],
    
    [6, 2, 0]
    
    ]

After a second pass, the remaining negative values can all be converted to positives:
    
    [
    
    [0, 2, 1],
    
    [5, 2, 0],
        
        [6, 2, 0]
        
        ]

Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't all be converted to positives, regardless of how many passes are run, your function should return -1.

Sample Input:

matrix = [

[0, -1, -3, 2, 0],
    
    [1, -2, -5, -1, -3],
    
    [3, 0, 0, -4, -1]
    
    ]

Sample Output:

3

"""


def minimumPassesOfMatrix(matrix):
    explore = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                explore.append([row, col])

                steps = [
                    [-1, 0],
                    [0, -1],
                    [1, 0],
                    [0, 1]
                ]
                count = -1
                while explore:
                    for _ in range(len(explore)):
                        row, col = explore.pop(0)
                        for step in steps:
                            next_row = row + step[0]
                            next_col = col + step[1]
                            if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]) and matrix[next_row][next_col] < 0:
                                matrix[next_row][next_col] *= -1
                                explore.append([next_row, next_col])

                    count += 1
    for row in matrix:
        for col in row:
            if col < 0:
                return -1
    return count


matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

print(minimumPassesOfMatrix(matrix))

