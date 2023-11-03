"""
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a
palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character
strings are palindromes.
Sample Input

string = "abcdcba"

Sample Output

true // it's written the same forward and backward


"""


#O(n^2) time | O(n) space


def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString


