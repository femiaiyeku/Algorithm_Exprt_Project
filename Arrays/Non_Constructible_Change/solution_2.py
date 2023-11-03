"""
Given an array of positive integers representing the values of coins in your possession, 
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. 
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value). 
For example, if you're given coins = [l, 2, S] , the minimum amount of change that you can't create is 4 .
 If you're given no coins, the minimum amount of change that you can't create is 1 . 


Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output
20


"""

# Time: O(nlogn) | Space: O(1)  - where n is the number of coins

def nonConstructibleChange(coins):
    coins.sort()

    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            return minimum_change + 1

        minimum_change += coin


    return minimum_change + 1

print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])) # 20

print(nonConstructibleChange([1, 1, 1, 1, 1])) # 6

print(nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100])) # 55

print(nonConstructibleChange([6, 4, 5, 1, 1, 8, 9])) # 3

print(nonConstructibleChange([1, 2, 3, 4, 5, 6, 7])) # 29

print(nonConstructibleChange([1])) # 2

print(nonConstructibleChange([2])) # 1

print(nonConstructibleChange([])) # 1

print(nonConstructibleChange([87])) # 1

print(nonConstructibleChange([5, 6, 1, 1, 2, 3, 4, 9])) # 32

print(nonConstructibleChange([5, 6, 1, 1, 2, 3, 43, 9])) # 19

print(nonConstructibleChange([1, 1, 1, 1, 1, 1])) # 7

print(nonConstructibleChange([1, 1, 1, 1, 1, 2])) # 10

print(nonConstructibleChange([2, 3, 4, 5])) # 1

print(nonConstructibleChange([1, 1, 1, 1, 1])) # 6

print(nonConstructibleChange([1, 1, 1, 1, 1])) # 6
