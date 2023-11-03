"""

Phone Number Mnemonics

Almost every digit is associated with some leners in the alphabet; this allows certain phone numbers to spell out actual words. For example, the phone number 8464747328 can be written as timisgreat; similarly, the phone number 2686463 can be wrinen as antoi ne or as ant6463 . 
It's important to note that a phone number doesn't represent a single sequence of letters, but rather multiple combinations of letters. For instance, the digit 2 can represent three different letters (a, b, and c). 
A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something. Companies oftentimes use a mnemonic for their phone number to make it easier to remember. 
Given a stringified phone number of any non-zero length, write a function that returns all mnemonics for this phone number, in any order. 
For this problem, a valid mnemonic may only contain letters and the digits e and 1 . In other words, if a digit is able to be represented by a lener, then it must be. Digits e and 1 are the only two digits that don't have letter representations on the keypad. 
Note that you should rely on the keypad illustrated above for digit-letter associations. 


Sample Input    : "1905"

Sample Output   : [ 
                    "1w0j",
                    "1w0k",
                    "1w0l",
                    "1x0j",
                    "1x0k",
                    "1x0l",
                    "1y0j",
                    "1y0k",
                    "1y0l",
                    "1z0j",
                    "1z0k",
                    "1z0l",
                ]

"""

def nonAttackingQueens(n):
    blockedColumns = set()
    blockedUpDiagonals = set()
    blockedDownDiagonals = set()
    return getNumberOfNonAttackingPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)

def getNumberOfNonAttackingPlacements(row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize):
    if row == boardSize:
        return 1
    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
            placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
            validPlacements += getNumberOfNonAttackingPlacements(row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize)
            removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
    return validPlacements


def isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    if col in blockedColumns:
        return False
    if row + col in blockedUpDiagonals:
        return False
    if row - col in blockedDownDiagonals:
        return False
    return True

def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.add(col)
    blockedUpDiagonals.add(row + col)
    blockedDownDiagonals.add(row - col)

def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.remove(col)
    blockedUpDiagonals.remove(row + col)
    blockedDownDiagonals.remove(row - col)


if __name__ == "__main__":
    print(nonAttackingQueens(4))

    

