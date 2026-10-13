class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1) # contains indices 0 ... n
        for i in range(n+1):
            for j in range(i - 1, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j)) #itself, split and split again, split and take
        return dp[n]