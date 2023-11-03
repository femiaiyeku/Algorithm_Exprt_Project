"""

Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, 
write a function that returns the number of ways to make change for that target amount using the given coin denominations. 
Note that an unlimited amount of coins is at your disposal. 


Sample Input: n = 6, denoms = [1, 5]

Sample Output: 2 // 1x1 + 1x5 and 6x1



"""

def numberOfWaystoMakeChange(n, denoms):
    memo = [[ -1 for _ in range(n + 1)] for _ in range(len(denoms))]
    return numberOfWaysToMakeChangeHelper(n, denoms, 0, memo)

def numberOfWaysToMakeChangeHelper(n, denoms, index, memo):
    if n == 0:
        return 1
    if index >= len(denoms):
        return 0
    if memo[index][n] != -1:
        return memo[index][n]
    if denoms[index] <= n:
        memo[index][n] = numberOfWaysToMakeChangeHelper(n - denoms[index], denoms, index, memo) + numberOfWaysToMakeChangeHelper(n, denoms, index + 1, memo)
    else:
        memo[index][n] = numberOfWaysToMakeChangeHelper(n, denoms, index + 1, memo)
    return memo[index][n]


# O(nd) time | O(n) space

