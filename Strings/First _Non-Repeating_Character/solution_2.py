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
    characterFrequencies = {}
    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1


# O(n) time | O(1) space - where n is the length of the input string


