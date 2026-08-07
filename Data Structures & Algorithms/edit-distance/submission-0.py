class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        dp = [[float("inf")] * (N2 + 1) for _ in range(N1 + 1)]

        for j in range(N2 + 1):
            dp[N1][j] = N2 - j
        for i in range(N1 + 1):
            dp[i][N2] = N1 - i
        #fill in margins with base cases where at least one string is empty

        for i in range(N1 - 1, -1, -1):
            for j in range(N2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
        return int(dp[0][0])


