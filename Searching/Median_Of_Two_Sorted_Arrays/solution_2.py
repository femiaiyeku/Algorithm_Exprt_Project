"""

You're given two sorted arrays of integers arrayOne and arrayTwo. Write a
function that returns the median of these arrays.
You can assume both arrays have at least one value. However, they could be of
different lengths. If the median is a decimal value, it should not be rounded
(beyond the inevitable rounding of floating point math).

Sample Input:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output:
16


"""

def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    smallArray = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    bigArray = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo

    leftIdx = 0
    rightIdx = len(smallArray) - 1
    mergedLeftIdx = (len(smallArray) + len(bigArray) - 1) // 2 
    while True:
        smallPartitionIdx = (leftIdx + rightIdx) // 2
        bigPartitionIdx = mergedLeftIdx - smallPartitionIdx - 2

        smallLeft = smallArray[smallPartitionIdx] if smallPartitionIdx >= 0 else float("-inf")
        smallRight = smallArray[smallPartitionIdx + 1] if (smallPartitionIdx + 1) < len(smallArray) else float("inf")
        bigLeft = bigArray[bigPartitionIdx] if bigPartitionIdx >= 0 else float("-inf")
        bigRight = bigArray[bigPartitionIdx + 1] if ((bigPartitionIdx + 1) < len(bigArray)) else float("inf")

        if smallLeft <= bigRight and bigLeft <= smallRight:
            if (len(smallArray) + len(bigArray)) % 2 == 0:
                return (max(smallLeft, bigLeft) + min(smallRight, bigRight)) / 2
            else:
                return max(smallLeft, bigLeft)
        elif smallLeft > bigRight:
            rightIdx = smallPartitionIdx - 1
        else:
            leftIdx = smallPartitionIdx + 1
    # return -1 # unreachable code


