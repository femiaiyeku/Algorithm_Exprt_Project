"""
A company has hired N interns to each join one of N different teams. Each intern has ranked their preferences for which
teams they wish to join, and each team has ranked their preferences for which interns they prefer.
Given these preferences, assign 1 intern to each team. These assignments should be "stable," meaning that there is no
unmatched pair of an intern and a team such that both that intern and that team would prefer they be matched with
each other.
In the case there are multiple valid stable matchings, the solution that is most optimal for the interns should be chosen
(L.e. every intern should be matched with the best team possible for them).
Your function should take in 22-dimensional lists, one for interns and one for teams. Each inner list represents a single
intern or team's preferences, ranked from most preferable to least preferable. These lists will always be of length N.
with integers as elements. Each of these integers corresponds to the index of the team/intern being ranked. Your
function should return a 2-dimensional list of matchings in no particular order. Each matching should be in the format
[internindex, teamindex].


Sample Input
interns = [
[0, 1, 2],
[1, 0, 2],
[1, 2, 0]
]

teams = [
[0, 1, 2],
[1, 0, 2],
[1, 2, 0]
]

Sample Output

[
[0, 0],
[1, 1],
[2, 2]
]


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        interns = [
            [0, 1, 2],
            [1, 0, 2],
            [1, 2, 0]
        ]

        teams = [
            [0, 1, 2],
            [1, 0, 2],
            [1, 2, 0]
        ]

        output = ProgrammingError.stableInternships(interns, teams)

        self.assertTrue(len(output) == 3)

    def test_case_2(self):
        interns = [
            [0, 1, 2],
            [1, 0, 2],
            [1, 2, 0]
        ]

        teams = [
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0]
        ]

        output = ProgrammingError.stableInternships(interns, teams)

        self.assertTrue(len(output) == 3)

        
