def exist(board, word) -> bool:
    neighbours  = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m = len(board)
    n = len(board[0])
    
    def dfs(i, j, depth):
        print(board)
        if depth == len(word):
            return True     
        
        for neig in neighbours:
            next_step = (i+neig[0], j+neig[1])
            if 0<=next_step[0]<m and 0<=next_step[1]<n and board[next_step[0]][next_step[1]] == word[depth]:
                print("Next Step", depth, next_step[0], next_step[1], board[next_step[0]][next_step[1]])
                temp = board[next_step[0]][next_step[1]]
                board[next_step[0]][next_step[1]] = "#"
                # Changing the values being considered in the current path to #
                res =  dfs(next_step[0], next_step[1], depth+1)
                board[next_step[0]][next_step[1]] = temp
                if res:
                    return res
                else:
                    continue
        print("No Next Step", depth, word[depth])

        return False
            
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                print("Start", i, j, word[0])
                temp = board[i][j]
                board[i][j] = "#"
                res = dfs(i, j, 1)
                board[i][j] = temp
                if res:
                    return True
    
    return False
            
    
print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
#    0   1   2   3
# 0["A","B","C","E"],
# 1["S","F","E","S"],
# 2["A","D","E","E"]]