"""

In the game of Blackjack, the dealer must draw cards until the sum of the values of their cards is greater than or
equal to a target value minus 4. For example, traditional Blackjack uses a target value of 21, so the dealer
must draw cards until their total is greater than or equal to 17, at which point they stop drawing cards (they
"stand"). If the dealer draws a card that brings their total above the target (above 21 in traditional Blackjack),
they lose (they "bust").
Naturally, when a dealer is drawing cards, they can either end up standing or busting, and this is entirely up to the
luck of their draw.
Write a function that takes in a target value as well as a dealer's startingHand value and returns the
probability that the dealer will bust (go over the target value before standing). The target value will always
be a positive integer, and the startingHand value will always be a positive integer that's smaller than or equal
to the target value.
For simplicity, you can assume that the dealer has an infinite deck of cards and that each card has a value
between 1 and 10 inclusive. The likelihood of drawing a card of any value is always the same, regardless of
previous draws.
Your solution should be rounded to 3 decimal places and to the nearest value. For example, a probability of
0.314159 would be rounded to 0.314, while a probability of 0.1337 would be rounded to 0.134.

Sample Input
target = 21
startingHand = 10

Sample Output
0.583


"""

# Solution 1: Recursion
# Complexity Analysis
# O(2^n) time | O(n) space - where n is the target value

def blackjackProbability(target, startingHand):
    memo = {}
    return probabilityOfBusting(target - startingHand, memo)

def probabilityOfBusting(currentHand, target, memo):
    if currentHand > target:
        return 1
    if currentHand in memo:
        return memo[currentHand]
    probability = 0
    for cardValue in range(1, 11):
        probability += probabilityOfBusting(currentHand + cardValue, target, memo)
    probability /= 10
    memo[currentHand] = probability
    return probability


