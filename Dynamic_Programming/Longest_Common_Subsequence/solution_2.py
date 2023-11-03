"""
Write a function that takes in two strings and returns their longest common subsequence.
A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same
order as they appear in the string. For instance, the characters ["a", "c", "d"] form a subsequence of the string
"abcd", and so do the characters ["b", "d"]. Note that a single character in a string and the string itself are both
valid subsequences of the string.
You can assume that there will only be one longest common subsequence.


Sample Input:


str1 = "ZXVVYZW"
str2 = "XKYKZPW"


Sample Output:


["X", "Y", "Z", "W"]


"""

#O(nm*min(n,m)) time | O(nm*min(n,m)) space

def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenLcs = [[] for x in range(len(small) + 1)]
    oddLcs = [[] for x in range(len(small) + 1)]
    for i in range(1,len(big) + 1):
        if i % 2 == 1:
            currentLcs = oddLcs
            previousLcs = evenLcs
        else:
            currentLcs = evenLcs
            previousLcs = oddLcs
        for j in range(1,len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
            else:
                currentLcs[j] = max(previousLcs[j],currentLcs[j - 1],key = len)


    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]



