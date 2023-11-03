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


def stableInternships(interns, teams):

    N = len(interns)
    availableTeams = list(range(N))
    teamChoices = [0] * N
    internChoices = {}
    internRankings = []

    for teamIndex in range(N):
        for i, internNum in enumerate(teams[teamIndex]):
            internsArrayByCurrentTeam = {}
            for rankingIndex, internId in enumerate(interns[internNum]):
                internsArrayByCurrentTeam[internId] = rankingIndex
            internRankings.append(internsArrayByCurrentTeam)

    while len(availableTeams) > 0:
        currentIntern = availableTeams.pop(0)
        currentTeam = interns[currentIntern][teamChoices[currentIntern]]
        teamChoices[currentIntern] += 1

        if currentTeam not in internChoices:
            internChoices[currentTeam] = currentIntern
        else:
            currentInternInTeam = internChoices[currentTeam]
            if internRankings[currentTeam][currentIntern] < internRankings[currentTeam][currentInternInTeam]:
                internChoices[currentTeam] = currentIntern
                availableTeams.append(currentInternInTeam)


    return [[intern, team] for team, intern in internChoices.items()]

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

print(stableInternships(interns, teams))




