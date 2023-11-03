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
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

