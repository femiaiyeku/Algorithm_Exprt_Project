"""
Write a function that takes in an array of integers and returns a new array containing, at each index, the next element in the input array that's greater than the element at that index in the input array. 
In other words, your function should return a new array where outputArray [i J is the next element in the input array that's greater than i nputArray [ i J .
 If there's no such next greater element for a particular index, the value at that index in the output array should be -1 . For example, given array = (1, 2] , your function should return (2, -1] 
Additionally, your function should treat the input array as a circular array. A circular array wraps around itself as if it were connected end-to-end. 
So the next index after the last index in a circular array is the first index. This means that, for our problem, given array = (0, 0, s, 0, 0, 3, 0, 0] ,the next greater element after 3 is 5 ,since the array is circular. 


Sample Input

array = [2, 5, -3, -4, 6, 7, 2]

Sample Output
[5, 6, 6, 6, 7, -1, S]


"""

def nextGreaterElement(array):
    S, R = [], [-1 for _ in array]
    for i, e in enumerate(array):
        while S and S[-1][1] < e:
            R[S.pop()[0]] = e
        S.append([i, e])
    return R

# O(n) time | O(n) space     where n is the length of the input array



