"""

You're given two strings stringone and stringTwo. Write a function that determines if these two strings can
be made equal using only one edit.
There are 3 possible edits:
• Replace: One character in one string is swapped for a different character.
• Add: One character is added at any index in one string.
• Remove: One character is removed at any index in one string.
Note that both strings will contain at least one character. If the strings are the same, your function should return
true.

Sample Input
stringOne = "abc"

stringTwo = "ab"

Sample Output
true

Explanation 
We can make stringOne equal to stringTwo by removing the "c" from stringOne. 
Alternatively, we can make stringOne equal to stringTwo by deleting the "b" from stringTwo. 
Both of these edits are one edit away from stringOne and stringTwo.



"""

def oneEdit(s1, s2):
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            if len(s1) == len(s2):
                return s1[i+1:] == s2[i+1:]
            elif len(s1) < len(s2):
                return s1[i:] == s2[i+1:]
            else:
                return s1[i+1:] == s2[i:]
    return abs(len(s1) - len(s2)) == 1

print(oneEdit("abc", "ab"))
print(oneEdit("abc", "abc"))

