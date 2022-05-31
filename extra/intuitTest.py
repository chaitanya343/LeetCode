# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

# Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

# Sample input:

# user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
# user2 = ["a", "/one", "/two"]
# user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
# user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
# user5 = ["a"]
# user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

# Sample output:

# findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
# findContiguousHistory(user0, user2) => [] (empty)
# findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# findContiguousHistory(user2, user1) => ["a"] 
# findContiguousHistory(user5, user2) => ["a"]
# findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

# n: length of the first user's browsing history
# m: length of the second user's browsing history


user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


def calculateClicksByDomain(counts):
    result = {}
    for val in counts:
        count, url = val.split(",")
        subdomains = url.split(".")
        for i in range(len(subdomains), 0, -1):
            sd = ".".join(subdomains[i-1:])
            if sd in result:
                result[sd] += int(count)
            else:
                result[sd] = int(count)
    print(result)
    return result

import math

def findContiguousHistory(userX, userY):
    maxK = -math.inf
    maxXStart = None
    for ux in userX:
        for uy in userY:
            if ux == uy:
                ix = userX.index(ux)
                iy = userY.index(uy)
                checkMore = True
                k = 0
                while checkMore:
                    if ix+k<len(userX) and iy+k<len(userY) and userX[ix+k] == userY[iy+k]:
                        k+=1
                        #print("Match", userX[ix:ix+k], userY[iy:iy+k])
                    else:
                        #print("Broke", userX[ix:ix+k], userY[iy:iy+k])
                        checkMore = False
                if maxK<k:
                    maxXStart = ix
                    maxK = k
            #print(maxK, userX[maxXStart : maxXStart+maxK])
    return userX[maxXStart : maxXStart+maxK]
                        

print(findContiguousHistory(user0, user1))  
                

### Final


# Design and code a system that helps teams select the best engineer at any given moment. This system handles 3 types of requests:
# - Add an engineer for consideration
# - Hire the current highest-rated engineer
# - Hire the current highest-rated engineer who can start on or before N days

# An engineer has a unique id, an integer representing the days before they can start, and a list of 5 integers, ranging from 0 to 10, representing their skill ratings over 5 skills (example: software engineering, communication, etc). For simplicity, let’s ignore concurrency issues by assuming that only 1 request will be processed in the system at a time. 



import heapq
import math
skills = ['software engineering', 'communication']

class Engineer:
    
    def __init__(self, id, nToStart, skillList):
        self.id = id
        self.nToStart = nToStart
        self.skillList = skillList
    
    # def __repr__(self):
    #     return "Engineer: id="+str(self.id)+", nToStart="+int(self.nToStart)+", skillList="+str(self.skillList)
        
engineersForConsideration = []
engineersHired = []

def addEngineer(engineer):
    engineersForConsideration.append(engineer)

bestEngineers = []
heapq.heapify(bestEngineers)

for engg in engineersForConsideration:
    # bestEngineers.heappush(engg, -1 * sum(engg.skillList))
    heapq.heappush(bestEngineers, (engg, -1 * sum(engg.skillList)))

def hireBestEngineer(n = math.inf):
    if n == math.inf:
        engineersHired.append(heapq.heappop(bestEngineers))
    else:
        while bestEngineers:
            enggToHire = heapq.heappop(bestEngineers)
            if enggToHire.nToStart <= n:
                engineersHired.append(enggToHire)
                break
            
def main():
    addEngineer(Engineer(1, 1, [5, 5]))
    print("add 1", engineersForConsideration)
    addEngineer(Engineer(2, 3, [5, 5]))
    print("add 2", engineersForConsideration)
    addEngineer(Engineer(3, 10, [5, 10]))
    print("add 3", engineersForConsideration)
    
    hireBestEngineer()
    print("1", engineersHired)
    hireBestEngineer(2)
    print("2", engineersHired)
    hireBestEngineer(11)
    print("3", engineersHired)

main()

    