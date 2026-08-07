class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        if n == 3:
            return 2
        dp = [1] * (n+1)
        dp[1], dp[2], dp[3] = 1, 2, 3
        for i in range(4,n+1):
            for j in range(i-1,-1,-1):
                dp[i] = max(dp[i], (i - j) * dp[j])
        return dp[n]
