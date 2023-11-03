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

# Solution 2: Iterative Solution with Linear Time Complexity    O(n) time | O(1) space
#####################################################################################
#O(n + m) time | O(1) space

def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    idxOne, idxTwo = 0, 0
    middleIdx = (len(arrayOne) + len(arrayTwo)) // 2

    while idxOne + idxTwo < middleIdx - 1:
        if arrayOne[idxOne] < arrayTwo[idxTwo]:
            idxOne += 1
        else:
            idxTwo += 1

    if arrayOne[idxOne] < arrayTwo[idxTwo]:
        return arrayOne[idxOne]
    else:
        return arrayTwo[idxTwo]
    
# Solution 1: Recursive Solution with Logarithmic Time Complexity    O(log(n) + log(m)) time | O(log(n) + log(m)) space
#####################################################################################
#O(log(n) + log(m)) time | O(log(n) + log(m)) space
