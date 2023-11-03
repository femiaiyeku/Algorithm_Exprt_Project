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



#O(n) time | O(n) space  where n is the length of the number string

def bestDigits(number, numDigits):
    if numDigits >= len(number):
        return "0"
    digits = []
    for digit in number:
        while len(digits) > 0 and numDigits > 0 and digits[-1] < digit:
            digits.pop()
            numDigits -= 1
        digits.append(digit)
    while numDigits > 0:
        digits.pop()
        numDigits -= 1
    return "".join(digits).lstrip("0")




