"""
You're given a two-dimensional array (a matrix) of equal height and width that represents the exchange rates of arbitrary currencies. 
The length of the array is the number of currencies, and every currency can be converted to every other currency. Each currency is represented by a row in the array, 
where values in that row are the floating-point exchange rates between the row's currency and all other currencies, as in the example below. 

In the matrix above, you can see that row 0 represents USD, which means that row 0 contains the exchange rates for 1 USD to all other currencies. Since row 1 represents CAD, index 1 in the USD row contains the exchange for 1 USD to CAD. The currency labels are listed above to help you visualize the problem, but they won't actually be included in any inputs and aren't relevant to solving this problem. 
Write a function that returns a boolean representing whether an arbitrage opportunity exists with the given exchange rates. An arbitrage occurs if you can start with C units of one currency and execute a series of exchanges that lead you to having more than C units of the same currency you started with. 
Note: currency exchange rates won't represent real-world exchange rates, and there might be multiple ways to generate an arbitrage. 

Sample Input

exchangeRates = [
    [1.0, 0.8631, 0.5903],
    [1.1587, 1.0, 0.6849],
    [1.6939, 1.46, 1.0]
]

Sample Output

true

"""


from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1.0, 0.8631, 0.5903],
            [1.1587, 1.0, 0.6849],
            [1.6939, 1.46, 1.0]
        ]
        expected = True
        actual = ProgrammingError.detectArbitrage(input)
        self.assertEqual(actual, expected)





