class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    obstacleGrid[r][c] = 1
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                if r > 0:
                    obstacleGrid[r][c] += obstacleGrid[r-1][c]
                if c > 0:
                    obstacleGrid[r][c] += obstacleGrid[r][c-1]

        return obstacleGrid[-1][-1]