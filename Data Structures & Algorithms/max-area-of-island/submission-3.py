class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxIsland = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            curr = 1
            for dr, dc in directions:
                curr += dfs(r + dr, c + dc)
            return curr

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    currIsland = dfs(r, c)
                    maxIsland = max(currIsland, maxIsland)

        return maxIsland