"""
Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order. 
If the input array is empty, the function should return an empty array. 

Sample Input:

array = [1, 2, 3]

Sample Output:
    
    [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
    ]

    



"""

#O(n*n!) time | O(n*n!) space

def getPermutations(array):

    def helper(array):
        if len(array) == 1:
            yield array

            for idx, element in enumerate(array):
                remianing = array[:idx] + array[idx+1:]
                for sub_perm in helper(remianing):
                    yield [element] + sub_perm

                    return list(helper(array))
                

array = [1, 2, 3]
print(getPermutations(array))

