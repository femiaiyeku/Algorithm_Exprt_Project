"""
Write a function that takes in a string made up of parentheses ( (and) ). The function should return an integer
representing the length of the longest balanced substring with regards to parentheses.
A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no
parenthesis is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes before
it, and similarly, a closing parenthesis can't match an opening parenthesis that comes after it.

Sample Input
string = "(()))("

Sample Output
4 // The longest balanced substring is "(())".





"""


def longestBalancedSubstring(string):
    maxLengths = [0 for _ in string]
    for i in range(1, len(string)):
        if string[i] == ")":
            if string[i-1] == "(":
                maxLengths[i] = maxLengths[i-2] + 2
            elif i - maxLengths[i-1] > 0 and string[i-maxLengths[i-1]-1] == "(":
                maxLengths[i] = maxLengths[i-1] + 2 + maxLengths[i-maxLengths[i-1]-2]
    return max(maxLengths) if len(maxLengths) > 0 else 0



#O(n) time | O(1) space   where n is the length of the input string


