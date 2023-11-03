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
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])

    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]



