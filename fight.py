from difflib import SequenceMatcher

# def findLength(a, b):
#     if len(a)>len(b):
#         base, searcher = a, b
#     else:
#         base, searcher = b, a

#     maxSubArrayCount = 0
#     for i, s in enumerate(searcher):
#         for j, b in enumerate(base):
#             print(s, b)
#             if s == b:
#                 print("first match")
#                 subArrayCount = 1
#                 while s == b and i+1<len(searcher) and j+1<len(base):
#                     print(s,b)
#                     s = searcher[i+1]
#                     b = base[j+1]
#                     subArrayCount+=1
#                     i+=1
#                     j+=1
#                 print(subArrayCount)
#                 if subArrayCount > maxSubArrayCount:
#                     maxSubArrayCount = subArrayCount

#     return maxSubArrayCount

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
b = [1,1,1,0,1]
# print(findLength(a, b))
# print(dp(a, b))
print(findLength(a, b))
