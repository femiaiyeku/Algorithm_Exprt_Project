"""
One of the most efficient ways to run a factory is to use an assembly line, with multiple stations
performing different assembling steps simultaneously in order to save time. But an assembly line
only as fast as its slowest station/step; for example, if an assembly line has 100 different steps
performed by 100 different stations, with 99 steps taking 1 minute each to complete and 1 step ta
1 hour to complete, then the entire assembly line is dramatically slowed down by the 1-hour-long
step.
Write a function that takes in a non-empty array of positive Integers stepDurations and a positive
integer numStations. The Input array of Integers represents the times that the various steps in
assembly process take, and the Input Integer represents the number of stations that this assembl
process has access to. For this particular assembly process, a single station can perform multiple
steps, so long as these steps are performed in order, meaning that a single station can perform
multiple steps whose times appear consecutively in the stepDurations array. Your function
should return the longest duration of a single station in the assembly line after optimizing the
assembly line (1.e., minimizing its slowest station/step).
You can assume that there will never be more stations than steps.


Sample Input:
stepDurations = [15,15 30, 30, 45]
numStations = 3

Sample Output:

60

"""

def optimalAssemblyLine(stepDurations, numStations):
    left, right = max(stepDurations), sum(stepDurations)
    maxStationDuration = float("inf")

    while left <= right:
        potentialMaxStationDuration = (left + right) // 2

        if canProduceRequiredUnitsInTime(stepDurations, numStations, potentialMaxStationDuration):
            maxStationDuration = potentialMaxStationDuration
            right = potentialMaxStationDuration - 1
        else:
            left = potentialMaxStationDuration + 1
            
    return maxStationDuration


def canProduceRequiredUnitsInTime(stepDurations, numStations, maxStationDuration):
    numStationsUsed = 1
    stationDuration = 0
    for stepDuration in stepDurations:
        if stationDuration + stepDuration > maxStationDuration:
            numStationsUsed += 1
            stationDuration = 0
        stationDuration += stepDuration
    return numStationsUsed <= numStations




    
