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


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = ProgrammingError.SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {
                "c": {"*": True},
                "a": {"b": {"c": {"*": True}}},
                "*": True
            },
            "a": {"b": {"c": {"*": True}}},
            "*": True
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))
        self.assertTrue(trie.contains("c"))
        self.assertTrue(trie.contains("bc"))
        self.assertTrue(trie.contains("ab"))
        self.assertFalse(trie.contains("d"))
        self.assertFalse(trie.contains("abcx"))
        self.assertFalse(trie.contains("f"))
        self.assertFalse(trie.contains("q"))
        self.assertFalse(trie.contains("y"))
        self.assertFalse(trie.contains("abcz"))
        self.assertFalse(trie.contains("abcde"))
        self.assertFalse(trie.contains("babcde"))

        # O(n^2) time | O(n^2) space


