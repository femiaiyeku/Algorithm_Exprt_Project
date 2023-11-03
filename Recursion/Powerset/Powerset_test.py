"""
Write a function that takes in an array of unique integers and returns its powerset. 
The powerset P (X) of a set X is the set of all subsets of X . For example, the powerset of [ 1, 2] is 
[[], [1], [2], [1,2]] 
Note that the sets in the powerset do not need to be in any particular order. 

Sample Input: [1, 2, 3]



Sample Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = sorted(ProgrammingError.powerset([]))
        self.assertEqual(output, [[]])

    def test_case_2(self):
        output = sorted(ProgrammingError.powerset([1]))
        self.assertEqual(output, [[], [1]])

    def test_case_3(self):
        output = sorted(ProgrammingError.powerset([1, 2]))
        self.assertEqual(output, [[], [1], [2], [1, 2]])

    def test_case_4(self):
        output = sorted(ProgrammingError.powerset([1, 2, 3]))
        self.assertEqual(output, [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_case_5(self):
        output = sorted(ProgrammingError.powerset([1, 2, 3, 4]))
        self.assertEqual(
            output,
            [
                [],
                [1],
                [2],
                [3],
                [4],
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
                [1, 2, 3],
                [1, 2, 4],
                [1, 3, 4],
                [2, 3, 4],
                [1, 2, 3, 4],
            ],
        )

        



