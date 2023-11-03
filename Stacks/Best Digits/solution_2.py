"""
Write a function that takes a positive integer represented as a string number and an integer numDigits-
Remove numDigits from the string so that the number represented by the string is as large as possible
afterwards.
Note that the order of the remaining digits cannot be changed. You can assume numDigits will always be
than the length of number and greater than or equal to 0.

Sample Input

number = "1432219"

numDigits = 3

Sample Output
"2219"

"""

def bestDigits(number, numDigits):
    l = len(number)
    i = 0
    L = []
    number = list(number)
    L.append(number[0])
    for i in range(1,len(number)):
        if number[i] > L[-1]:
            L.pop()
            L.append(number[i])
        else:
            L.append(number[i])

    return "".join(L).lstrip("0")


#O(n) time | O(n) space  where n is the length of the number string
