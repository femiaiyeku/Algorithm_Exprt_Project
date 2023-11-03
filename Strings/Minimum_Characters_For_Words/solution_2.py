"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of
the words. The characters don't need to be in any particular order.
For example, the characters ["y", "r", "o", "u"] are needed to form the words
["your", "you", "or", "yo"].
Note: the input words won't contain any spaces; however, they might contain punctuation and/or special
characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]

Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]


"""


def minimumCharactersForWords(words):
    mainMap = {}
    resultList = []
    tempMap = {}
    for letter in words:
        if letter not in mainMap:
            mainMap[letter] = 0
        mainMap[letter] += 1
    for letter in words:
        tempMap = {}
        for char in letter:
            if char not in tempMap:
                tempMap[char] = 0
            tempMap[char] += 1
        for char in tempMap:
            if char in mainMap:
                if tempMap[char] > mainMap[char]:
                    mainMap[char] = tempMap[char]
            else:
                mainMap[char] = tempMap[char]
    for char in mainMap:
        for i in range(mainMap[char]):
            resultList.append(char)
    return resultList

