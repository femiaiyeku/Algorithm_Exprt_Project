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


# Time O(n^2) | Space O(n^2) - where n is the number of interns and teams

def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoice = [0] * len(interns)

    teamMaps = []
    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)

        while len(freeInterns) > 0:
            intern = freeInterns.pop(0)
            team = interns[intern][currentInternChoice[intern]]
            currentInternChoice[intern] += 1

            if team not in chosenInterns:
                chosenInterns[team] = intern
                break
            else:
                currentIntern = chosenInterns[team]
                if teamMaps[team][intern] < teamMaps[team][currentIntern]:
                    chosenInterns[team] = intern
                    freeInterns.append(currentIntern)


    return [[intern, team] for team, intern in chosenInterns.items()]






    