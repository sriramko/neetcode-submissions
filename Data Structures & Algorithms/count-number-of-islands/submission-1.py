class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def inGrid(row, col) -> bool:
            return row < ROWS and row >= 0 and col < COLS and col >= 0
        
        def bfs(row, col) -> None:
            if not inGrid(row, col) or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for dx, dy in dirs:
                bfs(row + dx, col + dy)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        return res