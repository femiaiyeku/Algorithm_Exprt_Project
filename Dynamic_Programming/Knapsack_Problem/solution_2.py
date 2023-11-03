"""
You're given an array of arrays where each subarray holds two integer values and represents an item; the first integer is
the item's value, and the second integer is the item's weight. You're also given an integer representing the maximum
capacity of a knapsack that you have.
Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity, all the
while maximizing their combined value. Note that you only have one of each item at your disposal.
Write a function that returns the maximized combined value of the items that you should pick as well as an array of the
indices of each item picked.
If there are multiple combinations of items that maximize the total value in the knapsack, your function can return any
of them.


Sample Input:
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

Sample Output:
[10, [1, 3]] // items [4, 3] and [6, 7]

// The values in the array are ordered according to the indices in the input array

"""


# O(nc) time | O(nc) space


VALUE_IDX = 0
ITEMS_IDX = 1


def knapsackProblem(items, capacity):
    DP = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]  
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                DP[i][c] = DP[i - 1][c]
            else:
                DP[i][c] = max(DP[i - 1][c], DP[i - 1][c - currentWeight] + currentValue)

    return [DP[-1][-1], getKnapsackItems(DP, items)]

def getKnapsackItems(DP, items):
    sequence = []
    i = len(DP) - 1
    c = len(DP[0]) - 1
    while i > 0:
        if DP[i][c] == DP[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


if __name__ == "__main__":
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    print(knapsackProblem(items, capacity))
    # [10, [1, 3]] // items [4, 3] and [6, 7]
    # // The values in the array are ordered according to the indices in the input array

    items = [[465, 100], [400, 85], [255, 55], [350, 45], [650, 130], [1000, 190], [455, 100], [100, 25], [1200, 190], [320, 65], [750, 100], [50, 45], [550, 65], [100, 50], [600, 70], [240, 40]]

    capacity = 200
    print(knapsackProblem(items, capacity))
    