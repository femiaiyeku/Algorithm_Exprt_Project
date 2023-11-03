"""
Write a function that takes in a non-empty, unordered array of positive Integers and returns the array's
majority element without sorting the array and without using more than constant space.
An array's majority element is an element of the array that appears in over half of its indices. Note that the
most common element of an array (the element that appears the most times in the array) isn't necessarily the
array's majority element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 13 both have 2 as
their most common element, yet neither of these arrays have a majority element, because neither 2 nor any
other element appears in over half of the respective arrays' indices.
You can assume that the input array will always have a majority element.


Sample Input
array= [1, 2, 3, 2, 2, 1, 2]

Sample Output

2   // 2 appears more than 3 times in the input array, and no other number appears more than 3 times in the input array.



"""

def majorityElement(array):
    # Write your code here
   answer = 0 

   for currentBit in range(32):
       numOnes = 0
       for num in array:
           if num & (1 << currentBit) != 0:
               numOnes += 1
       if numOnes > len(array) // 2:
           answer |= 1 << currentBit
    return answer if answer < (1 << 31) else answer - (1 << 32)

