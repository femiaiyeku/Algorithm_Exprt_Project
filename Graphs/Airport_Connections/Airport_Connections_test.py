"""
For the purpose of this question, the phrases "airport route" and "airport connection" are used interchangeably

You·re given a list of alrportS (three-letter codes like "JFK" ), a list of routes (one-way nights from one airport to another like 
["JFK", "SFO"] ), and a starting airport. 
Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order for someone to be able to reach any airport in the list, starting at the starting airport. 
Note that routes only allow you to fly in one direction; for instance, the route ["JFK", "SFO"] only allows you to fly from 
11JFK11 to "SFO11 
Also note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting airport by stopping at other airports first. 

Sample Input

airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

routes = [
["DSM", "ORD"],
["ORD", "BGI"],
["BGI", "LGA"],
["SIN", "CDG"],
["CDG", "SIN"],
["CDG", "BUD"],
["DEL", "DOH"],
["DEL", "CDG"],
["TLV", "DEL"],
["EWR", "HND"],
["HND", "ICN"],
["HND", "JFK"],
["ICN", "JFK"],
["JFK", "LGA"],
["EYW", "LHR"],
["LHR", "SFO"],
["SFO", "SAN"],
["SFO", "DSM"],
["SAN", "EYW"]
]

startingAirport = "LGA"

Sample Output
3 // of the following routes: 
["LGA", "TLV"], ["LGA", "CDG"], ["LGA", "SFO"]

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        AIRPORTS = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND",
                    "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN",
                    "TLV", "BUD"]
        
    STARTING_AIRPORT = "LGA"

    ROUTES = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
    ]

    expected = 3

    self.assertEqual(ProgrammingError.airportConnections(AIRPORTS, ROUTES, STARTING_AIRPORT), expected)





