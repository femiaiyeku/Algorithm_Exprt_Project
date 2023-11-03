"""
Write a function that takes 1n an array of integers and returns the largest possible value for the expression 
array[a] - array[b] + array[c] - array[d] ,where a, b, c ,and d areindices ofthe array and a< b < c < d

if  the input array has fewer than 4 elements, your function should return 0

Sample Input

array = [3, 6, 1, -3, 2, 7]


Sample Output

4 // by choosing a = 1, b = 3, c = 4, and d = 5


"""


#O(n ^ 4) time | O(1) space

def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maximumValue = float("-inf")
    for a in range(len(array) - 3):
        for b in range(a + 1, len(array) - 2):
            for c in range(b + 1, len(array) - 1):
                for d in range(c + 1, len(array)):
                    currentExpressionValue = array[a] - array[b] + array[c] - array[d]
                    maximumValue = max(maximumValue, currentExpressionValue)
    return maximumValue



