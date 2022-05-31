from difflib import SequenceMatcher

def findLengthBrute(a, b):
    if len(a)>len(b):
        base, searcher = a, b
    else:
        base, searcher = b, a

    baseStarts = {}
    for i, b in enumerate(base):
        if b in baseStarts:
            baseStarts[b].append(i)
        else:
            baseStarts[b] = [i]
    
    maxSubArrayCount = 0
    for i, s in enumerate(searcher):
        for j in baseStarts[s]:
                k=0
                while i+k<len(searcher) and j+k<len(base) and searcher[i+k] == base[j+k]:
                    k+=1
                maxSubArrayCount = max(k, maxSubArrayCount)

    return maxSubArrayCount

def dp(A, B):
    longest = 0
    DP = [[0] * (len(B)+1) for _ in range(len(A) + 1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                DP[i][j] = 1+DP[i-1][j-1]
                longest = max(longest, DP[i][j])
    print(DP)
    return longest

def findLength(A, B):
        if set(A).isdisjoint(B): return 0
        a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(0, len(A), 0, len(B))
        return size

a = [0,1,1,1,1]
b = [1,0,1,0,1]
print(findLengthBrute(a, b))
# print(dp(a, b))
# print(findLength(a, b))
