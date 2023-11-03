"""
Minesweeper is a popular video game. From Wikipedia, "The game features a grid of clickable squares, with hidden "mines" scattered
throughout the board. The objective is to clear the board without detonating any mines, with help from clues about the number of neighboring
mines in each field." Specifically, when a player clicks on a square (also called a cell) that doesn't contain a mine, the square reveals a number
representing the number of immediately adjacent mines (including diagonally adjacent mines).
You're given a two-dimensional array of strings that represents a Minesweeper board for a game in progress. You're also given a row and a
column representing the indices of the next square that the player clicks on the board. Write a function that returns an updated board after the
click (your function can mutate the input board).
The board will always contain only strings, and each string will be one of the following:
● "N":Amine that has not been clicked on.
"X": A mine that has been clicked on, indicating a lost game.
4
• "H": A cell with no mine, but whose content is still hidden to the player.
• "8-8":A cell with no mine, with an integer from 0 to 8 representing the number of adjacent mines. Note that this is a single-digit integer
represented as a string. For example "2" would mean there are 2 adjacent cells with mines. Numbered cells are not clickable as they
have already been revealed.
If the player clicks on a mine, replace the "M" with "X", Indicating the game was lost.
If the player clicks on a cell adjacent to a mine, replace the "H" with a string representing the number of adjacent mines.
If the player clicks on a cell with no adjacent mines, replace the "H" with "e". Additionally, reveal all of the adjacent hidden cells as if the player had clicked on those cells as well
If the player clicks on a cell that isn't represented by the input board, do nothing.

Sample Input:
board = [
["E", "E", "E", "E", "E"],
["E", "E", "M", "E", "E"],
["E", "E", "E", "E", "E"],
["E", "E", "E", "E", "E"]]
click = [3, 0]
Sample Output:
[
["B", "1", "E", "1", "B"],
["B", "1", "M", "1", "B"],
["B", "1", "1", "1", "B"],
["B", "B", "B", "B", "B"]]
Explanation:
5

Sample Input:
board = [
["B", "1", "E", "1", "B"],
["B", "1", "M", "1", "B"],
["B", "1", "1", "1", "B"],
["B", "B", "B", "B", "B"]]
click = [1, 2]
Sample Output:
[
["B", "1", "E", "1", "B"],
["B", "1", "X", "1", "B"],
["B", "1", "1", "1", "B"],
["B", "B", "B", "B", "B"]]
Explanation:
6
"""

from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["E", "E", "E", "E", "E"],
            ["E", "E", "M", "E", "E"],
            ["E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E"]]
        click = [3, 0]
        expected = [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"]]
        actual = ProgrammingError.revealMinesweeper(board, click)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

    
