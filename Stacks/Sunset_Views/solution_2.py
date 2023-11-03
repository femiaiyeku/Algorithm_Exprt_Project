"""
Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the buildings that can see the sunset. 
A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces. 
The input array named buildings contains positive, non-zero integers representing the heights of the buildings. A building at index i thus has a height denoted by buildings [i] . All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named di rec ti on , which will always be equal to either "EAST" or "WEST" . In relation to the input array, you can interpret these directions as right for east and left for west. 
Important note: the indices in the ouput array should be sorted in ascending order. 

Sample Input
buildings =[3, 5, 4, 4, 3, 1, 3, 2) 
direction = "EAST" 

Sample Output 

[1, 3, 6, 7]


"""

def sunsetViews(buildings, direction):
    result = []
    if direction == "EAST":
        start = len(buildings) - 1
        step = -1
    else:
        start = 0
        step = 1
    maxHeight = 0
    idx = start
    while idx >= 0 and idx < len(buildings):
        if buildings[idx] > maxHeight:
            result.append(idx)
        maxHeight = max(maxHeight, buildings[idx])
        idx += step
    if direction == "WEST":
        return result[::-1]
    return result

#O(n) time | O(n) space

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST"))

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST") == [0, 1])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST") == [0, 1])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST") == [0, 1])

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7])


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST") == [0, 1])


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7])


    