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

import collections, itertools

def airportConnections(airports, routes, startingAirport):
    G = {x: set() for x in airports}
    for s, d in routes: G[s].add(d)
    # print(G)

    def reachable(r):
        V, Q = set(), [r]
        while Q:
            n = Q.pop()
            if n not in V:
                V.add(n)
                Q += G[n] - V
        return V
    
    R = reachable(startingAirport)
    # print(R)
    # print(len(R))
    # print(len(airports))
    # print(len(R) == len(airports))

    # print(G)
    # print(G.keys())
    # print(G.values())
    # print(G.items())
    # print(G.items()[0])
    # print(G.items()[0][0])
    # print(G.items()[0][1])
    # print(G.items()[0][1].difference(R))
    # print(G.items()[0][1].difference(R) == set())
    # print(G.items()[0][1].difference(R) == set([]))
    # print(G.items()[0][1].difference(R) == set([]) and G.items()[0][0] not in R)
    # print(G.items()[0][1].difference(R) == set([]) and G.items()[0][0] not in R and G.items()[0][0] not in R)
    # print(G.items()[0][1].difference(R) == set([]) and G.items()[0][0] not in R and G.items()[0][0] not in R and G.items()[0][0] not in R)
    # print(G.items()[0][1].difference(R) == set([]) and G.items()[0][0] not in R and G.items()[0][0] not in R and G.items()[0][0] not in R and G.items()[0][0] not in R)
