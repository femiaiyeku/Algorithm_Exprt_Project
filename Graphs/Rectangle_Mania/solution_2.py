"""
Write a function that takes In a list of Cartesian coordinates {i.e., {x, y) coordinates) 
and returns the number of rectangles formed by these coordinates. 
A rectangle must have its four corners amongst the coordinates in order to be counted, 
and we only care about rectangles with sides parallel to the x and y axes 
{i.e., with horizontal and vertical sides--no diagonal sides). 
You can also assume that no coordinate will be farther than 100 units from the origin 


Sample Input
coordinates = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0]
]

Sample Output

6 // 6 rectangles can be formed by these coordinates:

// 1: [[0, 0], [0, 1], [1, 1], [1, 0]]



"""

def rectasngleMania(coords):
    coords_set = set([x, y] for x, y in coords)
    coords_table = get_coords_table(coords)
    return get_rectangle_count(coords, coords_table)

def get_coords_table(coords):
    coords_table = {}
    for coord1 in coords:
        coord1_directions = {
            "right": [],
            "up": []
        }
        for coord2 in coords:
            coord2_direction = get_coord_direction(coord1, coord2)
            if coord2_direction in coord1_directions:
                coord1_directions[coord2_direction].append(coord2)
        coord1_string = coord_to_string(coord1)
        coords_table[coord1_string] = coord1_directions
    return coords_table


def get_coord_direction(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    if y2 == y1:
        return "right" if x2 > x1 else "left"
    return "up" if y2 > y1 else "down"

def coord_to_string(coord):
    x, y = coord
    return str(x) + "-" + str(y)

def get_rectangle_count(coords, coords_table):
    rectangle_count = 0
    for coord in coords:
        rectangle_count += clockwise_count_rectangles(coord, coords_table, "up", coord)
    return rectangle_count


def clockwise_count_rectangles(coord, coords_table, direction, origin):
    coord_string = coord_to_string(coord)
    if direction == "left":
        rectangle_found = origin in coords_table[coord_string]["left"]
        return 1 if rectangle_found else 0
    else:
        rectangle_count = 0
        next_direction = getNextClockwiseDirection(direction)
        for next_coord in coords_table[coord_string][direction]:
            rectangle_count += clockwise_count_rectangles(next_coord, coords_table, next_direction, origin)
        return rectangle_count
    
def getNextClockwiseDirection(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    return "up"



if __name__ == "__main__":
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0]
    ]
    print(rectasngleMania(coords)) # 6
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]
    ]
    print(rectasngleMania(coords)) # 1
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0]
    ]
    print(rectasngleMania(coords)) # 3
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0],
        [1, 3],
        [3, 3],
        [1, -1],
        [3, -1]
    ]
    print(rectasngleMania(coords)) # 6
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0],
        [1, 3],
        [3, 3],
        [1, -1],
        [3, -1],
        [-1, 1],
        [-1, 3],
        [4, 1],
        [4, 3]
    ]
    print(rectasngleMania(coords)) # 9
    coords = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0],
        [1, 3],
        [3, 3],
        [1, -1],
        [

            3, -1],
        [-1, 1],
        [-1, 3],
        [4, 1],
        [4, 3],
        [0, 4],
        [1, 4],
        [0, -1],
        [1, -1]
    ]
    print(rectasngleMania(coords)) # 18
    