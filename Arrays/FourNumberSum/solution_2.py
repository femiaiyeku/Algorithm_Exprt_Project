""" Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all 
these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should return an empty array.
Sample Input
array = [7, 6, 4, -1, 1, 2]

targetSum = 16
Sample Output
((7, 6, 4, -1), (7, 6, 1, 2)) """





def fourNumberSum (array, targetSum):
     # O(n^2) time | O(n^2) space
    result = []
    array.sort()
    for i in range (len(array) - 3):
        for j in range (i + 1, len(array) - 2):
            left = j + 1
            right = len(array) - 1
            while left < right:
                currentSum = array[i] + array[j] + array[left] + array[right]
                if currentSum == targetSum:
                    result.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                elif currentSum > targetSum:
                    right -= 1
    return result


