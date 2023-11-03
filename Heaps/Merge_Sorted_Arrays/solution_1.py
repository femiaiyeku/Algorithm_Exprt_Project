"""
Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all of
those arrays.
The integers in the merged list should be in sorted order.

Sample Input:
arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]
]

Sample Output:
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]


"""

#O(nk) time | O(n + k) space where n is the total number of elements in all the arrays and k is the number of arrays

def mergeSortedArrays(arrays):
    sortedList = []
    elementIdxs = [0 for array in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):
            relevantArray = arrays[arrayIdx]
            elementIdx = elementIdxs[arrayIdx]
            if elementIdx == len(relevantArray):
                continue
            smallestItems.append({
                "arrayIdx": arrayIdx,
                "num": relevantArray[elementIdx]
            })
        if len(smallestItems) == 0:
            break
        nextItem = getMinValue(smallestItems)
        sortedList.append(nextItem["num"])
        elementIdxs[nextItem["arrayIdx"]] += 1

    return sortedList

def getMinValue(items):
    minValueIdx = 0
    for i in range(1, len(items)):
        if items[i]["num"] < items[minValueIdx]["num"]:
            minValueIdx = i
    return items[minValueIdx]


