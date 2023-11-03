"""
Write a function that takes in two strings: a main string and a potential substring of the main string.
The function should return a version of the main string with every instance of the substring in it wrapped between underscores. 
If two or more instances of the substring in the main string overlap each other or sit side by side, 
the underscores relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost substring. 
If the main string doesn't contain the other string at all, the function should return the main string intact. 


Sample Input
string = "testthis is a testtest to see if testestest it works"
substring = "test"

Sample Output

"_test_this is a _testtest_ to see if _testestest_ it works"


"""
def underscorifySubstring(string, substring):
    idx_open =  -1
    idx_close = -1
    idx = 0
    out = ""
    while idx < len(string):
        if string[idx:idx+len(substring)] == substring:
            if idx_open == -1:
                idx_open = idx
            idx_close = idx+len(substring)
        else:
            if idx_open != -1:
                out += string[idx_open:idx_close] + "_"
                idx_open = -1
                idx_close = -1
            out += string[idx]
        idx += 1


    if idx_open != -1:
        out += string[idx_open:idx_close] + "_"
    return out

string = "testthis is a testtest to see if testestest it works"
substring = "test"
print(underscorifySubstring(string, substring))


# def getLocations(string, substring):
#     locations = []
#     startIdx = 0
#     while startIdx < len(string):
#         nextIdx = string.find(substring, startIdx)

#         if nextIdx != -1:
#             locations.append([nextIdx, nextIdx + len(substring)])
#             startIdx = nextIdx + 1
#         else:
#             break
#     return locations

    