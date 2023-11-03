"""
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by
summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent
numbers (numbers next to each other in the input array).



Sample Input

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]



Sample Output

19 // sum of the subarray: [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]


"""

def kadanesAlgorithm(array):
    curSum = array[0]
    maxSum = array[0]

    for num in array[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum
