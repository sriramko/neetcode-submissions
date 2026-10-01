class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                up = grid[r - 1][c] if r > 0 else float("inf")
                left = grid[r][c - 1] if c > 0 else float("inf")
                grid[r][c] += min(up, left)

        return grid[ROWS - 1][COLS - 1]