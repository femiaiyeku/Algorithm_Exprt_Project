"""

Write a function that takes in a list of unique strings and returns a list of semordnilap pairs. 
A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap". 
The order of the returned pairs an:J the order of the strings within each pair does not matter. 

Sample Input
words = ["code", "edoc", "da", "d"]

Sample Output

[["code", "edoc"], ["da", "d"]]



"""

def semordnilapPairs(words):
    arr = []
    map = {}
    for word in words:
        if word[::-1] in map:
            arr.append([word, word[::-1]])
        else:
            map[word] = True

    return arr

