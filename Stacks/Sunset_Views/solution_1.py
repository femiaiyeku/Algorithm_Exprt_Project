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


#O(n) time | O(n) space

def sunsetViews(buildings, direction):
    buildingsWithSunsetViews = []
    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1
    idx = startIdx
    runningMaxHeight = 0
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]
        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)
        runningMaxHeight = max(runningMaxHeight, buildingHeight)
        idx += step
    if direction == "EAST":
        return buildingsWithSunsetViews[::-1]
    return buildingsWithSunsetViews

#O(n) time | O(n) space



