"""

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity. 
Note that the strings are not guaranteed to only contain alphanumeric charaaers. The list you return can be in any order. 

Sample Input 

strings = ["abc", "bcd", "cbaccd"]

Sample Output
    
    ["b", "c"]


"""

def commonCharacters(strings):
    characterCounts = {}
    for string in strings:
        for character in string:
            if character in characterCounts:
                characterCounts[character] += 1
            else:
                characterCounts[character] = 1
    commonCharacters = []
    for character in characterCounts:
        if characterCounts[character] == len(strings):
            commonCharacters.append(character)

    return commonCharacters

strings = ["abc", "bcd", "cbaccd"]


print(commonCharacters(strings))

# Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string

# Space Complexity: O(c) where c is the number of unique characters across all strings

# This is the most optimal solution because it is the most time efficient and space efficient.

# This solution is optimal because it is the most time efficient and space efficient. It is time efficient because it only iterates through each string once and it is space efficient because it only stores the number of unique characters across all strings.

