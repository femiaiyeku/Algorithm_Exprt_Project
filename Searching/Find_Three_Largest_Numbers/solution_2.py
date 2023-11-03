"""

Write a function that takes in an array of at least three integers and, 
without sorting the input array, returns a sorted array of the three largest integers 1n the input array. 
The function should return duplicate integers 1f necessary; for example, 1t should return [10, 18, 12] for an input array of 

[10, 5, 9, 10,12]

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output:
[18, 141, 541]


"""

#o(w + h) time | O(1) space
def maximumSumSubmatrix(matrix):
    sums =[[0 for col in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + \
                sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
            
    return sums



def findThreeLargestNumbers(array):
    # Write your code here.
    output = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        updateLargest(output, num)
    return output

def updateLargest(output, num):
    if num > output[2]:
        shiftAndUpdate(output, num, 2)
    elif num > output[1]:
        shiftAndUpdate(output, num, 1)
    elif num > output[0]:
        shiftAndUpdate(output, num, 0)

    
def shiftAndUpdate(output, num, idx):
    for i in range(idx + 1):
        if i == idx:
            output[i] = num
        else:
            output[i] = output[i + 1]


            


