class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[nums[0],0]] + [[0,0] for _ in range(N-1)]
        for i in range(1, len(nums)):
            dp[i][0] = nums[i] + dp[i-1][1]
            dp[i][1] = max(dp[i-1][0],dp[i-1][1])
        return max(dp[-1])