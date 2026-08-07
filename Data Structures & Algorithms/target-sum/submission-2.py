class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]

        dp[0][0] = 1 # 1 way to sum to 0 using first 0 elements

        for i in range(n):
            for cursum, count in dp[i].items():
                dp[i + 1][cursum + nums[i]] += count
                dp[i + 1][cursum - nums[i]] += count
        
        return dp[n][target]