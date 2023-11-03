"""
You recently started freelance software development and have been offered a variety of job opportunities. Each job has
a deadline, meaning there is no value in completing the work after the deadline. Additionally, each job has an associated
payment representing the profit for completing that job. Given this information, write a function that returns the
maximum profit that can be obtained in a 7-day period.
Each job will take 1 full day to complete, and the deadline will be given as the number of days left to complete the job.
For example, if a job has a deadline of 1, then it can only be completed if it is the first job worked on. If a job has a
deadline of 2, then it could be started on the first or second day.
Note: There is no requirement to complete all of the jobs. Only one job can be worked on at a time, meaning that in
some scenarios it will be impossible to complete them all.


Sample Input:

jobs = [
    {"deadline": 2, "profit": 100},
    {"deadline": 1, "profit": 19},
    {"deadline": 2, "profit": 27},
    {"deadline": 1, "profit": 25},
    {"deadline": 3, "profit": 15}

]

Sample Output:
3 // Job 2, then Job 1, then Job 3


"""

#O(n^2) time | O(n) space - where n is the number of jobs

def optimalFreelance(jobs):
    jobs.sort(key=lambda x: x["profit"], reverse=True)
    maxProfit = 0
    jobTime = [0 for _ in range(7)]
    for job in jobs:
        for i in reversed(range(job["deadline"])):
            if i < len(jobTime) and jobTime[i] == 0:
                jobTime[i] = job["profit"]
                maxProfit += job["profit"]
                break
    return maxProfit


#O(nlog(n)) time | O(n) space - where n is the number of jobs

