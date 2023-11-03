"""
Write a function that takes in an array of non-negative integers and returns a sorted version of that array. 
Use the Radix Sort algorithm to sort the array. 
If you're unfamiliar with Radix Sort,
 we recommend watching the Conceptual Overview seaion of this question's video explanation before starting to code 

Sample Input
array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

Sample Output

[2, 12, 65, 87, 234, 345, 654, 3008, 8762]


"""


#O(d * (n + b)) time | O(n + b) space   where d is the max number of digits, n is the length of the array, and b is the base of the numbering system used

#d is the max number of digits, n is the length of the array, and b is the base of the numbering system used

def radixSort(array):
    if not len(array):
        return array
    maxValue = max(array)
    digit = 0
    numDigits = len(str(maxValue))
    while maxValue / 10 ** digit > 0:
        countingSort(array, digit, numDigits)
        digit += 1


def countingSort(array, digit, numDigits):
    numberDict = {}
    digitColumn = 10 ** digit
    for value in array:
        key = (value // digitColumn) % 10
        if key in numberDict:
            numberDict[key].append(value)
        else:
            numberDict[key] = [value]
    arrayIdx = 0
    for key in range(10):
        if key in numberDict:
            values = numberDict[key]
            for value in values:
                array[arrayIdx] = value
                arrayIdx += 1


                