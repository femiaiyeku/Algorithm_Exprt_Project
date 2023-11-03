""" Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The
function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all
these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves
should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.


Sample Input:
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0


Sample Output:
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

#O(n^2) time | O(n) space

def threeNumberSum(array, targetSum):

    array.sort()
    res = []

    for i in range(len(array)):
        twoSum(array, i, res, targetSum)
        return res
    def twoSum(array, i, res, targetSum):
        l, r = i + 1, len(array) - 1
        while l < r:
            currentSum = array[i] + array[l] + array[r]
            if currentSum == targetSum:
                res.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif currentSum < targetSum:
                l += 1
            elif currentSum > targetSum:
                r -= 1
    return res


                   