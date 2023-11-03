"""
Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the
big string. The function should return an array of booleans, where each boolean represents whether the small
string at that index in the array of small strings is contained in the big string.
Note that you can't use language-built-in string-matching methods.


Sample Input
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

Sample Output
[true, false, true, true, false, true, false]

// Note: the booleans in the array don't have to be in any particular order.




"""


# O(b^2 + ns) time | O(b^2 + n) space

def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True
    


# O(ns + bs) time | O(ns) space

