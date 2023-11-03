"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array. 
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), 
at which point they become strictly decreasing. At least three integers are required to form a peak. 
For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 
1, 2, 2, 0 . Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3. 

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output
6 // 0, 10, 6, 5, -1, -3


"""

def longestPeak(array):
    longest_peak = 0
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
           peak_length = getPeakLength(i, array)
           longest_peak = max(longest_peak, peak_length)
    return longest_peak

def getPeakLength(i, array, left = False):
    try:
        if not left and array[i] > array[i + 1]:
            return 1 + getPeakLength(i + 1, array, left = True) + getPeakLength(i +1, array)
        elif left and array[i] > array[i - 1]:
            return 1 + getPeakLength(i - 1, array, left = True) + getPeakLength(i -1, array)
        else:
            return 1
    except IndexError:
        return 1
    
    

