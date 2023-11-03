"""
Write a function that takes in an array of unique integers and returns its powerset. 
The powerset P (X) of a set X is the set of all subsets of X . For example, the powerset of [ 1, 2] is 
[[], [1], [2], [1,2]] 
Note that the sets in the powerset do not need to be in any particular order. 

Sample Input: [1, 2, 3]



Sample Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


"""

# O(n*2^n) time | O(n*2^n) space

def powerset(array):
    powerSet = []
    for i in range(2 ** len(array)):
        subSet = []
        for j in range(len(array)):
            if i & (1 << j):
                subSet.append(array[j])
        powerSet.append(subSet)

    return powerSet

