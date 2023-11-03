"""
You walk into a theatre you're about to see a show in. 
The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. 
Naturally you'd like to sit in the seat that gives you the most space. You also would prefer this space to be evenly distributed on either side of you {e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats). 
Given the theatre row represented as an integer array, return the seat index of where you should sit. 
Ones represent occupied seats and zeroes represent empty seats. 
You may assume that someone is always sitting in the first and last seat of the row. 
Whenever there are two equally good seats, you should sit in the seat with the lower index.
If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes. 


Sample Input
seats = [1, 0, 0, 0, 1, 0, 1]

Sample Output
4

"""

#O (n) time | O (1) space

def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0

    left = 0
    while left < len(seats):
        if seats[left] == 0:
            right = left
            while right < len(seats) and seats[right] == 0:
                right += 1

            currSpace = right - left
            if left == 0 or right == len(seats):
                currSpace *= 2

            if currSpace > maxSpace:
                maxSpace = currSpace
                bestSeat = left + (currSpace // 2)

            left = right
        else:
            left += 1

    return bestSeat
