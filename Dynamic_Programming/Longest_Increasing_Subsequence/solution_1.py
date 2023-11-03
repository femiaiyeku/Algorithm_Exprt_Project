"""
Given a non-empty array of integers, write a function that returns the longest strictly-increasing subsequence in the
array.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array
[1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both
valid subsequences of the array.
You can assume that there will only be one longest increasing subsequence.

Sample Input:

array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

Sample Output:

[-24, 2, 3, 5, 6, 35]


"""


# O(n^2) time | O(n) space

# Solution 1: Dynamic Programming

# The idea behind this approach is relatively simple. Initialize an array, seq, of the same length as the input array,

# where seq[i] represents the longest increasing subsequence that ends with array[i]. Also, initialize an array,

# lengths, of the same length as the input array, where lengths[i] represents the length of the longest increasing

# subsequence that ends with array[i]. Note that at any given point in time, the longest increasing subsequence that


# ends with array[i] is not necessarily the same as the longest increasing subsequence that we've seen so far. For

# example, consider the input array [1, 2, 3, 4, 5, 6, 7, 8] . At index 4, the longest increasing subsequence is

# [1, 2, 3, 4, 5] , but the longest increasing subsequence that we've seen so far is [1, 2, 3, 4, 5, 6, 7, 8] . The

def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    lengths = [1 for x in array]
    maxLengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array, sequences, maxLengthIdx)


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


# O(nlog(n)) time | O(n) space

