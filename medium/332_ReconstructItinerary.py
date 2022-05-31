import collections

def findItinerary(tickets):

    ticMap = collections.defaultdict(list)
    for fr, to in tickets:
        ticMap[fr].append(to)
        ticMap[fr].sort(reverse=True)
    print(ticMap)

    def dfs(to):
        print(path, to)
        while len(ticMap[to])>0:
            destination = ticMap[to].pop()
            path.append(destination)
            dfs(destination)
            
    path = ["JFK"]
    dfs("JFK")
    return path

print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))