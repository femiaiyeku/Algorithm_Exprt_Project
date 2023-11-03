"""
Write a function that takes in a non-empty array of integers and returns an array of the same length, 
where each element in the output array is equal to the product of every other number in the input array. 
In other words, the value at output [ i] is equal to the product of every number in the input array other than i nput[i] 
Note that you're expected to solve this problem without using division. 

Sample Input
array = [5, 1, 4, 2]

Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4



"""

# O(n^2) time | O(n) space  - where n is the length of the input array

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    return products

