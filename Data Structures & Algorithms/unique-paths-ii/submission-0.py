class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1
        for r in range(ROWS):
            for c in range(COLS):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        
        return dp[-1][-1]