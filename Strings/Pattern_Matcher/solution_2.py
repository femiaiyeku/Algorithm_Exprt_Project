"""
You·re given two non-empty strings. The first one is a pattern consisting of only "x" sand/ or "y" s; the other one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern. 
A string S0 1s said to match a pattern 1f replacing all "x" s 1n the pattern with some non-empty substring Sl of S0 and replacing all "y" s 1n the pattern with some non-empty substring S2 of S0 yields the same string S0 
If the input stnng doesn't match the input pattern. the function should return an empty array; otherwise. 1t should return an array holding the strings Sl and S2 that represent "x" and "y" 1n the normal string, 1n that order. If the pattern doesn't contain any "x" s or "y" s, the respective letter should be represented by an empty string in the final array that you return. 
You can assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and 
"y" 1n the normal string. 


Sample Input

pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"

Sample Output

["go", "powerranger"]


"""

def patternMatcher(pattern, string):
    if len(pattern) == 0 or len(string) == 0:
        return []
    
    firstLetterA = pattern[0]
    amountofA = 1
    amountofB = 0
    firstIdxB = -1

    for idx, letter in enumerate(pattern):
        if letter == firstLetterA:
            amountofA += 1
        else:
            amountofB += 1
            if firstIdxB == -1:
                firstIdxB = idx

    if amountofB == 0:
        if len(string) % amountofA != 0:
            return []
        else:
            lenOfA = len(string) // amountofA
            a = string[:lenOfA]
            return [a, ""] if firstLetterA == "x" else ["", a]
    else:
        for lenOfA in range(1, len(string)):
            lenOfB = (len(string) - lenOfA * amountofA) / amountofB
            if lenOfB <= 0 or lenOfB % 1 != 0:
                continue
            lenOfB = int(lenOfB)
            a = string[:lenOfA]
            b = string[firstIdxB * lenOfA:firstIdxB * lenOfA + lenOfB]
            potentialMatch = map(lambda char: a if char == firstLetterA else b, pattern)
            if string == "".join(potentialMatch):
                return [a, b] if firstLetterA == "x" else [b, a]
    return []

# Solution 2: O(n^2 + m) time | O(n + m) space - where n is the length of the string and m is the length of the pattern


   


    
