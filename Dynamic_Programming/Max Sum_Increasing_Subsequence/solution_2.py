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


def maxSumIncreasingSubsequence(array):
    cache = {}
    def dp(i):
        if i == len(array) - 1:
            return (array[i], [array[i]])
        if i in cache:
            return cache[i]
        num = array[i]
        current_sum = num
        items = [num]
        for j in range(i + 1, len(array)):
            if array[j] > num:
                tmp_sum, tmp_items = dp(j)
                if tmp_sum + num > current_sum:
                    current_sum = tmp_sum + num
                    items = [num] + tmp_items
        cache[i] = (current_sum, items)
        return cache[i]
    max_sum = 0
    max_items = []
    for i in range(len(array)):
        tmp_sum, tmp_items = dp(i)
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            max_items = tmp_items
    return [max_sum, max_items]


