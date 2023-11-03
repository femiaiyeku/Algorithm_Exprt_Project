"""
Write a function that takes 1n an array of integers and returns the largest possible value for the expression 
array[a] - array[b] + array[c] - array[d] ,where a, b, c ,and d areindices ofthe array and a< b < c < d

if  the input array has fewer than 4 elements, your function should return 0

Sample Input

array = [3, 6, 1, -3, 2, 7]


Sample Output

4 // by choosing a = 1, b = 3, c = 4, and d = 5


"""


def maximizeExpression(array):
    if len(array) < 4:
        return 0


    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf"), float("-inf")]
    maxOfAMinusBPlusCMinusD = [float("-inf"), float("-inf"), float("-inf")]

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx - 1], array[idx])
        maxOfA.append(currentMax)

    for idx in range(1, len(array)):
        currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
        maxOfAMinusB.append(currentMax)

    for idx in range(2, len(array)):
        currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)

    for idx in range(3, len(array)):
        currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)

    return maxOfAMinusBPlusCMinusD[-1]


print(maximizeExpression([3, 6, 1, -3, 2, 7]))


