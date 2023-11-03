"""
Write a function that takes in a string and returns its longest substring without duplicate characters.
You can assume that there will only be one longest substring without duplication.

Sample Input

string = "clementisacap"

Sample Output

"mentisac"

"""

def longestSubstringWithoutDuplication(string):
    l, r = 0, 0
    visited = set()
    longest = ''
    while r < len(string):
        if string[r] in visited:
            visited.remove(string[l])
            l += 1
        else:
            visited.add(string[r])
            r += 1
            if len(visited) > len(longest):
                longest = string[l:r]

    return longest
