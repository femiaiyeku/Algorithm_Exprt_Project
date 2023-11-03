"""
You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These
integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the
total height of the stack. A disk must have a strictly smaller width, depth, and height than any other disk below it.
Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the
bottom disk. Note that you can't rotate disks; in other words, the integers in each subarray must represent
[width, depth, height] at all times.
You can assume that there will only be one stack with the greatest total height.


Sample Input:
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Sample Output:
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]




"""

def diskStacking(disks):
    max_order, cur_order = [], []
    max_value, cur_value = 0, 0
    sorted_disks = sorted(disks, key=lambda x: x[2])
    for i in range(len(sorted_disks)):
        cur_order.append(sorted_disks[i])
        cur_value += sorted_disks[i][2]
        for j in range(i+1, len(sorted_disks)):
            if sorted_disks[j][0] > cur_order[-1][0] and sorted_disks[j][1] > cur_order[-1][1]:
                cur_order.append(sorted_disks[j])
                cur_value += sorted_disks[j][2]
        if cur_value > max_value:
            max_value = cur_value
            max_order = cur_order
        cur_order = []
        cur_value = 0

    return max_order


if __name__ == "__main__":
    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    print(diskStacking(disks))

    


