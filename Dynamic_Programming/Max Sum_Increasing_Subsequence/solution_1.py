"""
Write a function that takes 1n a non-empty array of integers and returns the greatest sum that can be generated from a strictly-1ncreas1ng subsequence 
In the array as well as an array of the numbers 1n that subsequence. 
A subsequence of an array 1s a set of numbers that aren't necessarily adJacent 1n the array but that are 1n the same order as they appear in the array.
For instance, the numbers [l, 3, 4] form a subsequence of the array [l, 2, 3, 4] , and so do the numbers [2, 4] . 
Note that a single number 1n an array and the array itself are both valid subsequences of the array. 
You can assume that there will only be one increas1ng subsequence with the greatest sum. 


Sample Input:
array = [10, 70, 20, 30, 50, 11, 30]


Sample Output:
[110, [10, 20, 30, 50]]     // The subsequence [10, 20, 30, 50] is strictly 1ncreasing and yields the greatest sum: 110.



"""


# O(n^2) time | O(n) space

def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


