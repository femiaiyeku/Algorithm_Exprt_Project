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

#O(n) time | O(n) space

def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


#Solution 2

#O(n) time | O(n) space

def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


#Solution 3

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


