import collections
import math
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

def employeeFreeTime_withSort(schedule):
    # events = []
    # for employee in schedule:
    #     for inter in employee:
              # events.append((inter.start, inter.end))
    # events.sort()
    # print(events)
    pass

def employeeFreeTime(schedule):
    time = collections.defaultdict(int)
    maxLimit = -math.inf
    for employee in schedule:
        for inter in employee:
            for i in range(inter.start, inter.end):
                time[i] +=1 
                maxLimit = max(maxLimit, i)
    
    freeTimeSlotStarts = []
    for i in range(1, maxLimit):
        if i not in time:
            freeTimeSlotStarts.append(i)

    print("free",freeTimeSlotStarts)
    ans = []
    freeSlotStart, freeSlotEnd = freeTimeSlotStarts[0], None
    for j, f in enumerate(freeTimeSlotStarts):
        freeSlotEnd = f
        if freeSlotEnd+1 in freeTimeSlotStarts:
            continue
        else:
            ans.append([freeSlotStart, freeSlotEnd+1])
            if j+1 < len(freeTimeSlotStarts):
                freeSlotStart = freeTimeSlotStarts[j+1]
    return ans

schedule = [[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5)],[Interval(9,12)]]
print(employeeFreeTime(schedule))