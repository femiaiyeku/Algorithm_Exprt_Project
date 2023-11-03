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
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getCoordsTable(coords):
    coordsTable = {}
    for coord1 in coords:
        coord1Directions = {
            "right": [],
            "up": []
        }
        for coord2 in coords:
            coord2Direction = getCoordDirection(coord1, coord2)
            if coord2Direction in coord1Directions:
                coord1Directions[coord2Direction].append(coord2)
        coord1String = coordToString(coord1)
        coordsTable[coord1String] = coord1Directions
    return coordsTable


def getCoordDirection(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    if y2 == y1:
        return "right" if x2 > x1 else "left"
    return "up" if y2 > y1 else "down"

def coordToString(coord):
    x, y = coord
    return str(x) + "-" + str(y)

def getRectangleCount(coords, coordsTable):
    rectangleCount = 0
    for coord in coords:
        rectangleCount += clockwiseCountRectangles(coord, coordsTable, "up", coord)
    return rectangleCount

def clockwiseCountRectangles(coord, coordsTable, direction, origin):
    coordString = coordToString(coord)
    if direction == "left":
        rectangleFound = origin in coordsTable[coordString]["right"]
        return 1 if rectangleFound else 0
    else:
        rectangleCount = 0
        nextDirection = "left" if direction == "up" else "right"
        for nextCoord in coordsTable[coordString][direction]:
            rectangleCount += clockwiseCountRectangles(nextCoord, coordsTable, nextDirection, origin)
        return rectangleCount
    



    