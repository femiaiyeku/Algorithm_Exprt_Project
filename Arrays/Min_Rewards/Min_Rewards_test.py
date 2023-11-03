"""
Imagine that you·re a teacher who's jUSt graded the final exam 1n a class. You have a 11st of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: 
All students must rPce1vP at least one reward.
Any given student must receive strictly more rewards than an adjacent student (a student 1mmed1ately to the left or to the
right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score

Write a function that takes 1n a 11st of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules. 
You can assume that all students have different scores; ,n other words, the scores are all un,que. 

Sample Input
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]

Sample Output
25 // you should reward these students like [4, 3, 2, 1, 2, 3, 4, 5, 1]


"""



from sqlite3 import ProgrammingError
import unittest


class  TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ProgrammingError.minRewards([1]), 1)
        
