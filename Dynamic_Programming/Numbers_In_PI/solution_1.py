"""
Given a string representation of the first n d1g1ts of Pi and a 11st of positive integers (all 1n string format), 
write a function that returns the smallest number of spaces that can be added to the n d1g1ts of P1 such that all resulting numbers are found 1n the list of integers. 
Note that a single number can appear multiple times 1n the resulting numbers. For example, 1f P1 1s "3141" and the numbers are [" l", "3", "4"] , 
the number "l" 1s allowed to appear twice 1n the 11st of resulting numbers after three spaces are added: "3 I 1 I 4 I l" 
If no number of spaces to be added exists such that all resulting numbers are found 1n the 11st of integers, the function should return -1 


Sample Input
pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]

Sample Output
2 // "314159265 | 35897932384626433832 | 79"


"""

#O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers


def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)

    cache[idx] = minSpaces
    return cache[idx]


#O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers