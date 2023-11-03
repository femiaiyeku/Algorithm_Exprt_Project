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


def minRewards(scores):
    rewards = [1 for _ in scores]

    for i in range(len(scores) -1):
        if scores[i] < scores[i+1]:
            rewards[i+1] = rewards[i] + 1
            for i in reversed(range(i)):
                if scores[i] > scores[i+1]:
                    rewards[i] = max(rewards[i], rewards[i+1] + 1)
                else:
                    break
        elif scores[i] > scores[i+1]:
            rewards[i] = rewards[i+1] + 1
            for i in range(i+1, len(scores)-1):
                if scores[i] < scores[i+1]:
                    rewards[i+1] = rewards[i] + 1
                else:
                    break
    return sum(rewards)


    


