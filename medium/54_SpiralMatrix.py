
def spiralOrder(matrix):
    res = []
    
    if len(matrix) == 0:
        return res

    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1 
    col_end = len(matrix[0])-1

    # running till rows and cols don't overlap
    while (row_begin <= row_end and col_begin <= col_end):

        # Horizontal Right move
        for i in range(col_begin,col_end+1):
            res.append(matrix[row_begin][i])
        print(res)
        row_begin += 1

        # Vertical Down move
        for i in range(row_begin,row_end+1):
            res.append(matrix[i][col_end])
        print(res)
        col_end -= 1

        # Horizontal Left move
        if (row_begin <= row_end):
            for i in range(col_end,col_begin-1,-1):
                res.append(matrix[row_end][i])
            print(res)
            row_end -= 1
        
        # Vertical Up move
        if (col_begin <= col_end):
            for i in range(row_end,row_begin-1,-1):
                res.append(matrix[i][col_begin])
            print(res)
            col_begin += 1

    return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))