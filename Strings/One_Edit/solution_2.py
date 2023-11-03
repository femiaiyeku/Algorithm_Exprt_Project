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

def oneEdit(stringOne, stringTwo):
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)   
    if abs(lengthOne - lengthTwo) > 1:
        return False
    elif lengthOne == lengthTwo:
        return oneEditReplace(stringOne, stringTwo)
    elif lengthOne + 1 == lengthTwo:
        return oneEditInsert(stringOne, stringTwo)
    elif lengthOne - 1 == lengthTwo:
        return oneEditInsert(stringTwo, stringOne)
    return True

def oneEditReplace(stringOne, stringTwo):
    foundDifference = False
    for i in range(len(stringOne)):
        if stringOne[i] != stringTwo[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditInsert(stringOne, stringTwo):
    indexOne, indexTwo = 0, 0
    while indexOne < len(stringOne) and indexTwo < len(stringTwo):
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if indexOne != indexTwo:
                return False
            indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1
    return True

print(oneEdit("abc", "ab"))

print(oneEdit("abc", "abc"))

print(oneEdit("abc", "abcd"))
