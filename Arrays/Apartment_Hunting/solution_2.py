"""
You're looking to move into a new apartment on specific street, 
and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.
You also have a list of requirements: a list of buildings that are important to you. 
For instance, you might value having a school and a gym near your apartment. 
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. For instance, 
for every block, you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.
Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and 
that returns the location (the index) of the block that's most optimal for you.
If there are multiple most optimal blocks, your function can return the index of any one of them.

Sample Input
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
        },
    {
        "gym": True,
        "school": False,
        "store": False,
        },
    {
        "gym": True,
        "school": True,
        "store": False,
        },
    {
        "gym": False,
        "school": True,
        "store": False,
        },
    {
        "gym": False,
        "school": True,
        "store": True,
        },
    ]   
reqs = ["gym", "school", "store"]

Sample Output
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther

        """

# O(br) time | O(br) space - where b is the number of blocks and r is the number of requirements

def apartmentHunting(blocks, reqs):
    min_distances_from_blocks = list(map(lambda req: get_min_distances(blocks, req), reqs))
    max_distances_at_blocks = get_max_distances_at_blocks(blocks, min_distances_from_blocks)
    return get_idx_at_min_value(max_distances_at_blocks)

def get_min_distances(blocks, req):
    min_distances = [0 for block in blocks]
    closest_req_idx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closest_req_idx = i
        min_distances[i] = distance_between(i, closest_req_idx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest_req_idx = i
        min_distances[i] = min(min_distances[i], distance_between(i, closest_req_idx))
    return min_distances

def get_max_distances_at_blocks(blocks, min_distances_from_blocks):
    max_distances_at_blocks = [0 for block in blocks]
    for i in range(len(blocks)):
        min_distances_at_block = list(map(lambda distances: distances[i],
                                           min_distances_from_blocks))
        max_distances_at_blocks[i] = max(min_distances_at_block)
    return max_distances_at_blocks

def get_idx_at_min_value(array):
    idx_at_min_value = 0
    min_value = float("inf")
    for i in range(len(array)):
        current_value = array[i]
        if current_value < min_value:
            min_value = current_value
            idx_at_min_value = i
    return idx_at_min_value

def distance_between(a, b):
    return abs(a - b)
