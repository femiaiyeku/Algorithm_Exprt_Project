"""

Write a function that, given a string, returns its longest palindromic substring.
 A palindrome 1s defined as a string thats written the same forward and backward. 
 Note that single-character strings are palindromes. 
 You can assume that there will only be one longest palindromic substring

Sample Input
string = "abaxyzzyxf"

Sample Output

"xyzzyx"

"""

def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring

    return longest

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


