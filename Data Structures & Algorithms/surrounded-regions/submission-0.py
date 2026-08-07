class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or board[row][col] != "O":
                return
            board[row][col] = "T"
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                dfs(row+dr,col+dc)


        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X" 
                if board[i][j] == "T":
                    board[i][j] = "O"