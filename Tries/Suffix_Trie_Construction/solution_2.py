"""

Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be
the root node of the trie and should support:
• Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon
class instantiation, which should populate the root of the class.
• Searching for strings in the trie.
Note that every string added to the trie should end with the special endSymbol character: "*"
If you're unfamiliar with Suffix Tries, we recommend watching the Conceptual Overview section of this question's

video explanation before starting to code.
Sample Input (for creation):
string = "babc"

Sample Output (for creation) [The strings below are in no particular order]:

{
"c": {"*": True},
"b": {
"c": {"*": True},
"a": {"b": {"c": {"*": True}}},
"*": True
},

"a": {"b": {"c": {"*": True}}},
"*": True
}

Sample Input (for searching in the suffix trie above):
string = "abc"

Sample Output (for searching in the suffix trie above):
true


"""

class SufficTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
        
    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insertSubstringStartingAt(idx, string)

    def insert_substring_starting_at(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
    
    # O(m) time | O(1) space


    