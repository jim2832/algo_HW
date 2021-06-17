def is_valid_sudoku(board):
    for i in range(9):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            if board[i][j]!= 0 and board[i][j] in row:
                return False
                row[board[i][j]] = 1
            if board[j][i]!= 0 and board[j][i] in column:
                return False
                column[board[j][i]] = 1
            rc= row_cube+j//3
            cc = column_cube + j%3
            if board[rc][cc] in block and board[rc][cc]!= 0:
                return False
            block[board[rc][cc]]=1
    return True