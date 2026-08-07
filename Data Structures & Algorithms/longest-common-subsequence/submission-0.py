class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * m for _ in range(n)]
        for i2, char1 in enumerate(text1):
            for i1, char2 in enumerate(text2):
                if char1 == char2:
                    dp[i1][i2] = 1
                    if i1 > 0 and i2 > 0:
                        dp[i1][i2] += dp[i1 - 1][i2 - 1]
                    continue
                sub = 0
                if i1 > 0:
                    sub = max(sub, dp[i1 - 1][i2]) 
                if i2 > 0:
                    sub = max(sub, dp[i1][i2 - 1])
                dp[i1][i2] = sub
        return dp[-1][-1]
