"""
This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only has two measuring lines, a Low {L) line and a High {H) line. This means that these cups can't precisely measure and can only guarantee that the substance poured into them wil be between the Land H line. For example, you might have a measuring cup that has a Low line at 400ml and a high line at 435ml . This means that when you use this measuring cup, you can only be sure that what you're measuring is between 400ml and 435ml . 
You're given a list of measuring cups containing their low and high lines as well as one low integer and one high integer representing a range for a target measurement. Write a function that returns a boolean representing whether you can use the cups to accurately measure a volume in the specified [low, high] range {the range is inclusive). 
Note that: 

• 	Each measuring cup will be represented by a pair of positive integers [L, HJ , where 0 <= L <= H . 
• 	You'll always be given at least one measuring cup, and the low and high input parameters will always satisfy the following constraint: 0 <= low <= high . 
• 	Once you've measured some liquid, it will immediately be transferred to a larger bowl that will eventually {possibly) contain the target measurement. 
• 	You can't pour the contents of one measuring cup into another cup. 


Sample Input:
cups = [
[200, 210],
[450, 465],
[800, 850]
]

low = 2100
high = 2300

Sample Output:
true
// We use cup [450, 465] to measure three volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 900, High = 930
// Third measurement: Low = 1350, High = 1395
// This covers the range [2100, 2300] , so we return true .

Explanation 
The given solution works fine but I personally found It extremely confusing and hard to navigate, especially when one Is trying to master recursive algorithmic concepts. 
In the solution below. I've organised the recursive calls in a way that presents crystal clear base cases and recursive case. In more detail, the cases are: 

• 	Base case 1: We get a cache hit and know that the current combination of (low. high) cannot enter the desired range. Return False 
• 	Base case 2: We have exceeded the target range. Return False. 
• 	Base case 3: We have successfully entered the target range. Return True 
• 	Recursive case: Check each available cup and make a recursive call to find out if the new low and new high will be able to enter the target range. If It can, we can bubble up a True return value to the top of the call stack, otherwise we append the failed combInat1on to the set and keep trying. 

Another imponant note is that there Is no need to store a cache and boolean values, since as soon as we find a valid range, we stop the algorithm and return True to the top. We will only ever write to the cache 1f the current range failed to enter the target range, therefore we can JUSt use a set of failed combinations. 
More comments In the code. Hope this helps' 

"""
#O(nc) time | O(nc) space   where n is the number of cups and c is the capacity of the largest cup

def ambiguousMeasurements(cups, low, high):
    cache = {}
    return canMeasureInRange(cups, low, high, cache)

def canMeasureInRange(cups, low, high, cache):
    if (low, high) in cache:
        return cache[(low, high)]

    if low > high:
        return False

    canMeasure = False
    for cup in cups:
        cupLow, cupHigh = cup
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break

        newLow = max(low - cupLow, 0)
        newHigh = max(high - cupHigh, 0)

        canMeasure = canMeasureInRange(cups, newLow, newHigh, cache)
        if canMeasure:
            break

    cache[(low, high)] = canMeasure
    return canMeasure




