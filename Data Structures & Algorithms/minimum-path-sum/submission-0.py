class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = grid.copy()
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
        return dp[-1][-1]

        