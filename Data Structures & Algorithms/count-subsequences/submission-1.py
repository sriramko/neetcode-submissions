class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [[0] * (len(s) + 1) for _ in range(len(t))]
        dp.append([1 for _ in range(len(s) + 1)])

        for tidx in range(len(t)-1,-1,-1):
            for sidx in range(len(s)-1,-1,-1):
                dp[tidx][sidx] += dp[tidx][sidx + 1]
                if s[sidx] == t[tidx]:
                    dp[tidx][sidx] += dp[tidx + 1][sidx + 1]
        
        return dp[0][0]