"""
You're given a two-dimensional array that represents the structure of an indoor waterfall and a positive integer that represents the column that the waterfall's water source will start at. More specifically, the water source will start directly above the structure and will flow downwards. 
Each row in the array contains 0 s and 1 s, where a 0 represents a free space and a 1 represents a block that water can't pass through. You can imagine that the last row of the array contains buckets that the water will eventually flow into; thus, the last row of the array will always contain only 0 s. You can also imagine that there are walls on both sides of the structure, meaning that water will never leave the structure; it will either be trapped against a wall or flow into one of the buckets in the last row. 
As water flows downwards, if it hits a block, it splits evenly to the left and right-hand side of that block. In other words, 50% of the water flows left and 50% of it flows right. If a water stream is unable to flow to the left or to the right (because of a block or a wall), the water stream in question becomes trapped and can no longer continue to flow in that direction; it effectively gets stuck in the structure and can no longer flow downwards, meaning that 50% of the previous water stream is forever lost. 
Lastly, the input array will always contain at least two rows and one column, and the space directly below the water source (in the first row of the array) will always be empty, allowing the water to start flowing downwards. 

Explanation 
Time complexity: O(wA2*h) 
Space Complexity: O(w) 
The only part of this solution that consumes space is the recursive call stack which in the worst case 
will scale with the width of the array where the 1 s form a ladder from the top right to the bottom left corner. 
This is a breadth first sea ch algorithm. The time complexity is the exact same as that of the A Igo Expert solution. 
The traversal method is divided up into downward and sideways traversal for a clean readable implementation. 

Sample Input
array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
]
source = 3

Sample Output
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1, 0]



"""

#O(wA2*h) time | O(w) space - where w is the width of the array, A is the depth of the waterfall, and h is the height of the array

def waterfallStreams(array, source):
    rowAbove = array[0][:]
    rowAbove[source] = -1

    for row in range(1, len(array)):
        currentRow = array[row][:]

        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove < 0
            hasBlock = currentRow[idx] == 1

            if not hasWaterAbove:
                continue

            if not hasBlock:
                currentRow[idx] += valueAbove
                continue

            splitWater = valueAbove / 2

            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1:
                    break
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater
                    break

            leftIdx = idx
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break

        rowAbove = currentRow

    finalPercentages = list(map(lambda num: num * -100, rowAbove))
    return finalPercentages

