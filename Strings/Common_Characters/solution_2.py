"""

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity. 
Note that the strings are not guaranteed to only contain alphanumeric charaaers. The list you return can be in any order. 

Sample Input 

strings = ["abc", "bcd", "cbaccd"]

Sample Output
    
    ["b", "c"]


"""

def commonCharacters(strings):
    smallerstString = getSmallestString(strings)
    potentialCommonCharacters = list(smallerstString)

    for potentialCommonCharacter in potentialCommonCharacters:
        for string in strings:
            if potentialCommonCharacter not in string:
                potentialCommonCharacters.remove(potentialCommonCharacter)
                break
    return potentialCommonCharacters

def getSmallestString(strings):
    smallestLength = float("inf")
    smallestString = ""
    for string in strings:
        if len(string) < smallestLength:
            smallestLength = len(string)
            smallestString = string
    return smallestString


strings = ["abc", "bcd", "cbaccd"]

print(commonCharacters(strings))

# Time Complexity: O(n * m^2) where n is the number of strings and m is the length of the longest string

# Space Complexity: O(c) where c is the number of unique characters across all strings


# This solution is not optimal because it is not time efficient. It is not time efficient because it iterates through each string multiple times. It is space efficient because it only stores the number of unique characters across all strings.