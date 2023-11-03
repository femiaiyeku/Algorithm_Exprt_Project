"""

You're given a list of arbitrary jobs that need to be completed; these jobs are represented by distinct integers. 
You're also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is a prerequisite of the second one. 
In other words, the second job depends on the first one; it can only be completed once the first job is completed. 
Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in which the given jobs can be completed. 
If no such order exists, the function should return an empty array. 


Sample Input:
jobs = [1, 2, 3, 4]
deps = [
    [1, 2],
    [1, 3],
    [3, 2],
    [4, 2],
    [4, 3],
]

Sample Output:
[1, 4, 3, 2] or [4, 1, 3, 2]



"""
import collections

# O(j + d) time | O(j + d) space

def topologicalSort(jobs, deps):
    outDegree = collections.defaultdict(int)
    inDegree = collections.defaultdict(list)
    for dep in deps:
        src, dst = dep
        outDegree[src] += 1
        inDegree[dst].append(src)

        stack = []
        for job in jobs:
            if job not in outDegree:
                stack.append(job)

                result = []
                count = 0
                while len(stack) > 0:
                    terminalNode = stack.pop()
                    result.append(terminalNode)

                    for node in inDegree[terminalNode]:
                        outDegree[node] -= 1
                        if outDegree[node] == 0:
                            stack.append(node)
                            count += 1

                if count == len(jobs):
                    return result
                else:
                    return []
                

# O(j + d) time | O(j + d) space




