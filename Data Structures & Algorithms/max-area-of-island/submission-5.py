class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maximum = 0

        def sink(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + sink(r+1,c) + sink(r,c+1) + sink(r-1,c) + sink(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                maximum = max(maximum, sink(r,c))
        return maximum