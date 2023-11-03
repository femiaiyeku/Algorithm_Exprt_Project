"""
Write a function that takes in a positive integer n and returns the number of non-attacking placements of n queens on an n x n chessboard. 
A non-attacking placement is one where no queen can attack another queen in a single turn. In other words, 
it's a placement where no queen can move to the same position as another queen in a single turn. 
In chess, queens can move any number of squares horizontally, vertically, or diagonally in a single turn. 


The chessboard above is an example of a non-attacking placement of 4 queens on a 4x4 chessboard.
 For reference, there are only 2 non-attacking placements of 4 queens on a 4x4 chessboard. 

Sample Input:

n = 4

Sample Output:

2

"""

def nonAttackingQueens(n):

    count = 0
    posDiag = set()
    negDiag = set()
    cols = set()

    def helper(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or row + col in posDiag or row - col in negDiag:
                continue
            cols.add(col)
            posDiag.add(row + col)
            negDiag.add(row - col)
            helper(row + 1)
            cols.remove(col)
            posDiag.remove(row + col)
            negDiag.remove(row - col)

    helper(0)
    return count

# Time Complexity: O(n!)
# Space Complexity: O(n)
