"""
You're given the position of two knight pieces on an infinite chess board. Write a function that returns the minimum number of turns
required before one of the knights is able to capture the other knight, assuming the knights are working together to achieve this goal.
The position of each knight is given as a list of 2 values, the x and y coordinates. A knight can make 1 of 8 possible moves on any given turn.
Each of these moves involves moving in an "L" shape. This means they can either move 2 squares horizontally and 1 square vertically, or
they can move 1 square horizontally and 2 squares vertically. For example, if a knight is currently at position [0, 0], then it can move to any
of these 8 locations on its next move:
[
[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
]
A knight is able to capture the other knight when it is able to move onto the square currently occupled by the other knight.
Each turn allows each knight to move up to one time. For example, if both knights moved towards each other once, and then knightA
captures knightB on its next move, two turns would have been used (even though knightB never made its second move).


Sample Input:
knightA = [0, 0]
knightB = [4, 2]

Sample Output:
1 // knightA can move to [2, 1], and then knightB captures KnightA on its next turn by moving to [2, 1]


"""

def knightConnection(knightA, knightB):
    dx = abs(knightA[0] - knightB[0])
    dy = abs(knightA[1] - knightB[1])

    if dx == 1 and dy ==1:
        return 1
    if dx + dy == 1 or dx ==2 and dy == 2:
        return 2
    
    start = (dx //4) * 2 + dx % 4

    threshold_y =(dx + 3) //2 if dx % 2 else dx //2

    if dy < threshold_y:
        distance = start + (1 - 2* int(dx % 4 > 1)) * (dy % 2)
    else:
        distance = (dy - threshold_y) % 3 + start - int(dx % 4 >1) + (dy - threshold_y) // 3

    return (distance + 1) // 2



