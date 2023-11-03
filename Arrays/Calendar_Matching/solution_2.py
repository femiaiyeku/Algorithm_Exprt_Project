"""

Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and your co-worker's calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime] ), as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earl iestTime, latestTime] ). 
Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily bounds, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startT;me, endT;me] ) during which you could schedule the meeting, ordered from earliest time block to latest. 
Note that times will be given and should be returned in military time. For example: 8: 30 , 9: 01 , and 23: 56 . 
Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them to appear in a calendar application like Google Calendar. 


Sample Input
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'J, ['16:00', '18:00']] 
dai1yBoundsl = [ '9:00', '20:00' J 
ca1endar2 = [('10:00', '11:30'), ['12:30', '14:30'), ['14:30', '15:00'J, ['16:00', '17:00')) dai1yBounds2 = ['10:00', '18:30'] 
meetingDuration = 30 


Sample Output
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


"""

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    ans = []
    n1, n2 = len(calendar1), len(calendar2)
    p1, p2 = -1. -1
    while p1 < n1 - 1 and p2 < n2 - 1:
        # find the next free time slot
        s1 = dailyBounds1[0] if p1 == -1 else calendar1[p1][1]
        s2 = dailyBounds2[0] if p2 == -1 else calendar2[p2][1]
        if s1 == e1:
            p1 += 1
            continue
        if s2 == e2:
            p2 += 1
            continue
        inter = getIntersection(meetingDuration, calendar1[p1 + 1], calendar2[p2 + 1])
        if inter [0] is not None:
            ans.append(inter)
        
        minutes1 = timeToMinutes(calendar1[p1 + 1][1])
        minutes2 = timeToMinutes(calendar2[p2 + 1][1])
        if minutes1 < minutes2:
            p1 += 1
        else:
            p2 += 1
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], ans))

def getIntersection(meetingDuration, slot1, slot2):
    s1, e1 = slot1
    s2, e2 = slot2
    start = max(s1, s2)
    end = min(e1, e2)
    if end - start >= meetingDuration:
        return [start, end]
    return [None, None] 

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes

def minutesToTime(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    hoursString = str(hours)
    minutesString = '0' + str(minutes) if minutes < 10 else str(minutes)
    return hoursString + ':' + minutesString

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))



    