
class Node:

    def __init__(self, c, p) -> None:
        self.courseNumber  = c
        self.prerequisites = p

def canFinish_Graph(numCourses, prerequisites):
    pass 

def canFinish(numCourses, prerequisites):
    courseMap = {}
    coursesDone = set()
    for p in prerequisites:  
        if p[0] in courseMap:
            courseMap[p[0]].add(p[1])
        else:
            courseMap[p[0]] = { p[1] }
          
    for c in range(numCourses):
        if c not in courseMap:
            coursesDone.add(c)

    for _ in range(len(prerequisites)):
        for c, pSet in courseMap.items():
            if len(pSet & coursesDone) == len(pSet):
                coursesDone.add(c)
        
    print(courseMap)
    print(coursesDone)
    return len(coursesDone) == numCourses

print(canFinish(3, [[2,1],[1,0]]))


