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

def reverseWordsInString(string):
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)

    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1
        reverseListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1
    return "".join(characters)

def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1




