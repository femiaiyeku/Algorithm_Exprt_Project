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
    maximumCharacterFrequencies = {}
    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)
    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
    characterFrequencies = {}
    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0
        characterFrequencies[character] += 1
    return characterFrequencies


def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]
        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency


def makeArrayFromCharacterFrequencies(characterFrequencies):
    characters = []
    for character in characterFrequencies:
        frequency = characterFrequencies[character]
        for _ in range(frequency):
            characters.append(character)
    return characters


if __name__ == '__main__':
    words = ["this", "that", "did", "deed", "them!", "a"]
    print(minimumCharactersForWords(words))

    