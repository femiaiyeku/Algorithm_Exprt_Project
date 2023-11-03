"""
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating rhr1rr1rtPr 
The first non-repeating character i􀀖 the first character in a string that occurs only once. 
If the input string doesn't have any non-repeating characters, your function should return -1 . 


Sample Input


string = "abcdcaf"


Sample Output


1 // The first non-repeating character is "b" and is found at index 1.


"""

def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True
        if not foundDuplicate:
            return idx
        

    return -1


# O(n^2) time | O(1) space - where n is the length of the input string

