"""
Given a list of strings, write a function that returns the longest string chain that can be built from those strings. 
A string chain is defined as follows: let string A be a string in the initial array; 
if removing any single character from string A yields a new string B that's contained in the initial array of strings, 
then strings A and B form a string chain of length 2. Similarly, 
if removing any single character from string B yields a new string C that's contained in the initial array of strings, 
then strings A , B , and C form a string chain of length 3. 
The function should return the string chain in descending order (i.e., 
from the longest string to the shortest one). Note that string chains of length 1 don't exist; 
if the list of strings doesn't contain any string chain formed by two or more strings, the function should return an empty array. 
You can assume that there will only be one longest string chain. 


Sample Input

strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

Sample Output

["abcdef", "abcde", "abde", "ade", "ae"]



"""


#O(n * m^2 + nlog(n)) time | O(nm) space - where n is the number of strings and m is the length of the longest string

from collections import defaultdict

def longestStringChain(strings):
    strings.sort(key=len)
    hs = dict()
    for i, string in enumerate(strings):
        hs[string] = i
    dp = defaultdict(int)
    for string in strings:
        for i in range(len(string)):
            prev = string[:i] + string[i+1:]
            if prev in hs:
                dp[string] = max(dp[string], dp[prev] + 1)
    maxLen = max(dp.values())
    res = []
    for string in strings:
        if dp[string] == maxLen:
            res.append(string)
            maxLen -= 1
    return res[::-1]


if __name__ == "__main__":
    strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    print(longestStringChain(strings)) # ["abcdef", "abcde", "abde", "ade", "ae"]
    strings = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestStringChain(strings)) # ["bdca", "bda", "ba", "a"]
    strings = ["abcdefg", "abcdef", "abcde", "abcd", "abc", "ab", "a"]
    print(longestStringChain(strings)) # ["abcdefg", "abcdef", "abcde", "abcd", "abc", "ab", "a"]
    strings = ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g"]
    print(longestStringChain(strings)) # ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g"]
    strings = ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g", "abdfgi", "abdefgi", "abdefgj", "ce", "cefg", "abcdefgk"]
    print(longestStringChain(strings)) # ["abcdefgk", "abcdefg", "abdefgj", "abdefgi", "abdfgi", "abdfg", "bdfg", "bfg", "bg", "g


    
