"""
Write a function that takes in a non-negative integer n and returns the number of possible Binary Tree topologies that can be created with exactly n nodes. 
A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2 : a root node with a left node, and a root node with a right node. 
Note that when n is equal to 0 , there's one topology that can be created: the None I nul 1 node. 


Sample Input:
n = 3

Sample Output:
5


"""


# Solution 2: Recursion + Memoization

# Complexity: O(n^2) time | O(n) space

def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n <= 1:
        return 1
    dp =[0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]
