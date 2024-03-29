"""
Write a function that takes in an array of strings and groups anagrams together. 
Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams. 
Your function should return a list of anagram groups in no particular order. 


Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]


"""

def groupAnagrams(words):
    if len(words) == 0:
        return []
    
    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord


    result.append(currentAnagramGroup)

    return result

if __name__ == "__main__":
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))

    