"""

You're given a set of numDice dice, each with numSides sides, and a target integer, which represents a target
sum to obtain when rolling all of the dice and summing their values. Write a function that returns the total number of
dice-roll permutations that sum up to exactly that target value.
All three input values will always be positive integers. Each of the dice has an equal probability of landing on any
number from 1 to numSides. Identical total dice rolls obtained from different individual dice rolls (for example,
[2, 3] vs. [3, 2] ) count as different dice-roll permutations. If there's no possible dice-roll combination that sums
up to the target given the input dice, your function should return 0.


Sample Input


numDice = 2
numSides = 6
target = 7

Sample Output

6 // The following dice-roll permutations sum up to the target:



"""


def diceThrows(numDice, numSides, target):
    storedResults = [[0] * (target + 1) for _ in range(numDice + 1)]
    storedResults[0][0] = 1

    for currentNumDice in range(1, numDice + 1):
        for currentTarget in range(1, target + 1):
            for currentNumSides in range(1, numSides + 1):
                if currentNumSides <= currentTarget:
                    storedResults[currentNumDice][currentTarget] += storedResults[currentNumDice - 1][
                        currentTarget - currentNumSides]
                    
    return storedResults[-1][-1]



print(diceThrows(2, 6, 7))
print(diceThrows(3, 6, 7))
print(diceThrows(4, 6, 7))


