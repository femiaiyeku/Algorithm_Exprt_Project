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

# Solution 2: O(n^2 + m) time | O(n + m) space - where n is the length of the string and m is the length of the pattern

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
    if counts["y"] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            x = string[:lenOfX]
            y = string[yIdx:yIdx + lenOfY]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        lenOfX = len(string) / counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]
    return []


def getNewPattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))
    

def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos

