"""
You're given two non-empty strings: a big string and a small string. Write a function that returns the smallest substring in the big string that contains all of the small string's characters. 
Note that: 
• 	The substring can contain other characters not found in the small string. 
• 	The characters in the substri1g don't have to be in the same order as they appear in the small string. 
• 	If the small string has duplicate characters, the substring has to contain those duplicate characters {it can also contain more, but not fewer). 

You can assume that there will only be one relevant smallest substring

Sample Input
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"

Sample Output
"f$axb$"

"""

def smallestSubstringContaining(bigString, smallString):
    
    char_counts = {}
    for char in smallString:
        char_counts[char] = char_counts.get(char, 0) + 1

    win_counts = {}
    left = n_equal_counts = 0
    smallest = 0, len(bigString)
    for right, char in enumerate(bigString, start=1):
        if char not in char_counts:
            continue
        win_counts[char] = win_counts.get(char, 0) + 1
        if win_counts[char] == char_counts[char]:
            n_equal_counts += 1
        while n_equal_counts == len(char_counts):
            if right - left < smallest[1] - smallest[0]:
                smallest = left, right
            char = bigString[left]
            if char not in char_counts:
                left += 1
                continue
            if win_counts[char] == char_counts[char]:
                n_equal_counts -= 1
            win_counts[char] -= 1
            left += 1
    return bigString[smallest[0]:smallest[1]]

            

# O(b + s) time | O(b + s) space - where b is the length of the big string and s is the length of the small string