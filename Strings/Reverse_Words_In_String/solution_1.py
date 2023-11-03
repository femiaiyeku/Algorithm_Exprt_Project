"""
Write a function that takes in a string of words separated by one or more whites paces and returns a string that has these words in reverse order. For example, given the string "tim is great" , your function should return "great is tim" 
For this problem, a word can contain special characters, punctuation, and numbers. The words 1n the string will be separated by 
one or more wh1tespaces, and the reversed string must contain the same wh1tespaces as the original string. For example, given the string "whi tespaces 4" you would be expected to return "4 whitespaces11 
Note that you're nor allowed to to use any built-in split or reverse methods/functions. However, you are allowed to use a built-in join method/function. 
Also note that the input string 1sn·t guaranteed to always contain words 

Sample Input:
string = "AlgoExpert is the best!"

Sample Output:
"best! the is AlgoExpert"

"""

# Solution 1: O(n) time | O(n) space - where n is the length of the input string

def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
    words.append(string[startOfWord:])
    reverseList(words)
    return "".join(words)

def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
