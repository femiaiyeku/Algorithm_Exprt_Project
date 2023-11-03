"""
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters; this matrix represents a boggle board. 
You're also given a list of words. 
Write a function that returns an array of all the words contained in the boggle board. The final words don't need to be in any particular order. 
A word is constructed in the boggle board by connecting adJacent (horizontally, vertically, or diagonally) letters, 
without using any single letter at a given position more than once; while a word can of course have repeated letters,
 those repeated letters must come from different positions in the boggle board in order for the word to be contained in the board. 
 Note that two or more words are allowed to overlap and use the same letters in the boggle board. 


 
Sample Input
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
]
words = [
    "this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"
    ]
Sample Output
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
// The words could be ordered differently.


"""

def boggleBoard(board, words):
    res = []
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for word in words:
        finished = [False]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    dfs(board, x, y, word, 0, directions, finished)
                    if finished[0]:
                        res.append(word)
                        break
            if finished[0] == True:
                break
    return res

def dfs(x, y, seen , word, u, board, directions, finished):
  if u == len(word):
    return
  if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or seen[x][y] or board[x][y] != word[u]:
    return
  if u == len(word) - 1:
    finished[0] = True
    return
  seen[x][y] = True
  for d in directions:
    dfs(x + d[0], y + d[1], seen, word, u + 1, board, directions, finished)
  seen[x][y] = False

# def dfs(board, x, y, word, u, directions, finished):


                