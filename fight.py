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
    for ux in userX:
        for uy in userY:
            if ux == uy:
                ix = userX.index(ux)
                iy = userY.index(uy)
                print(ux, uy)
                checkMore = True
                k = 0
                while checkMore:
                    if ix+k<len(userX) and iy+k<len(userY) and userX[ix+k] == userY[iy+k]:
                        k+=1
                    else:
                        print("Broke", userX[ix+k], userY[iy+k])
                        checkMore = False
                maxK = max(maxK, k)
                print(userX[ix:ix+maxK])
                        

findContiguousHistory(user0, user1)    
                