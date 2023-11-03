"""
Given a non-empty string, write a function that returns the minimum number of cuts needed to perform on the string
such that each remaining substring is a palindrome.
A palindrome is defined as a string that's written the same forward as backward. Note that single-character strings are
palindromes

Sample Input:

string = "noonabbad"

Sample Output:

2 // noon | abba | d



"""

#o(n^2) time | o(n^2) space where n is the length of the input string

def palindromePartitioningMinCuts(string):
    palindromes =[[False for i in string] for j in string]

    for i in range(len(string)):
        palindromes[i][i] = True
        for length in range(2, len(string) + 1):
            leftIdx = i
            rightIdx = i + length - 1
            if rightIdx >= len(string):
                break
            if length == 2:
                palindromes[leftIdx][rightIdx] = string[leftIdx] == string[rightIdx]
            else:
                palindromes[leftIdx][rightIdx] = string[leftIdx] == string[rightIdx] and palindromes[leftIdx + 1][rightIdx - 1] 
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1

    return cuts[-1]

print(palindromePartitioningMinCuts("noonabbad"))
print(palindromePartitioningMinCuts("ababbbabbababa"))

