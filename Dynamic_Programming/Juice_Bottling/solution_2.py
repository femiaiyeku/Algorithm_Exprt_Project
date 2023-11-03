"""

You're given an array of integers prices of length n with the retail prices of various quantities of juice. Each index in this array corresponds to the price of that amount of juice. 
For example, prices [2] would be the retail price of 2 units of juice. 
You have n - 1 total units of juice. For example, if the length of prices is 5, then you would have 4 total units of juice. 
Write a function to determine the optimal way to bottle the Juice such that it maximizes revenue. 
This function should return a list of all of the Juice quantities required in ascending order. 
Note that the first value in the prices array will always be 0, because there is no value in no juice. All other values will be positive integers. 
Additionally, a larger quantity of juice will not always be more expensive than a smaller quantity. For simplicity, all of the test cases only have one possible solution. 





Sample Input:

prices = [0, 1, 3, 2]

Sample Output:

[1, 2]

Explanation:

The optimal solution is to bottle 1 unit of juice, then 2 units of juice.



"""

def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    solutions = [0] * numSizes

    for size in range(numSizes):
        for j in range(size + 1):
            if maxProfit[size] < prices[j] + maxProfit[size - j - 1]:
                maxProfit[size] = prices[j] + maxProfit[size - j - 1]
                solutions[size] = j + 1

    result = []
    size = numSizes - 1
    while size > 0:
        result.append(solutions[size])
        size -= solutions[size]


    return result[::-1]

print(juiceBottling([0, 1, 3, 2]))
print(juiceBottling([0, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10]))
print(juiceBottling([0, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11]))
print(juiceBottling([0, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]))



