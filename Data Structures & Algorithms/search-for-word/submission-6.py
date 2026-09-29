class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def inBoard(r,c):
            return r < ROW and r >= 0 and c < COL and c >= 0

        def backtrack(r,c,i):
            if i == len(word):
                return True
            if not inBoard(r,c) or board[r][c] != word[i]:
                return False
            board[r][c] = ""
            for dr, dc in dirs:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            board[r][c] = word[i]
            return False

        for r in range(ROW):
            for c in range(COL):
                if backtrack(r,c,0):
                    return True
        return False