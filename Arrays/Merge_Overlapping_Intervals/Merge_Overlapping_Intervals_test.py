"""

Write a function that takes in a non-empty array of arbitrary Intervals, merges any overlapping intervals, and 
returns the new Intervals in no particular order.Each interval interval is an array of two integers,
with interval [0] as the start of the interval and interval[1] as theend of the interval.Note that back-to-back intervals aren't considered to be overlapping.
 For example, [1, 5] and [6, 7] aren't overlapping,however, [1, 6] and [6, 7] are indeed overlapping.
Also note that the start of any particular interval will always be less than or equal to the end of that interval.


Sample Input
intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]

Sample Output
[
    [1, 2],
    [3, 8],
    [9, 10]
]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [
            [1, 2],
            [3, 5],
            [4, 7],
            [6, 8],
            [9, 10]
        ]
        expected = [
            [1, 2],
            [3, 8],
            [9, 10]
        ]
        actual = ProgrammingError.mergeOverlappingIntervals(intervals)
        self.assertEqual(actual, expected)