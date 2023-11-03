"""
Write a function that takes in an array of integers and returns an array of the same length, 
where each element in the output array corresponds to the number of integers in the input array 
that are to the right of the relevant index and that are strictly smaller than the integer at that index. 

In other words, the value at output [ i] represents the number of integers that are to the right of smallerthan input[i] . 

More formally, the value at output[i] is equivalent to the number of elements that are to the right of i and that are strictly smaller than input[i] .

Sample Input

array = [8, 5, 11, -1, 3, 4, 2]

Sample Output

[5, 4, 4, 0, 1, 1, 0]

// There are 5 integers smaller than 8 to the right of it.
// There are 4 integers smaller than 5 to the right of it.
// There are 4 integers smaller than 11 to the right of it.
// ...




"""

#O(n^2) time | O(n) space   where n is the length of the input array
def rightSmallerThan(array):
    rightSmallerThan = []
    for i in range(len(array)):
        rightSmallerCount = 0
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                rightSmallerCount += 1
        rightSmallerThan.append(rightSmallerCount)

    return rightSmallerThan

