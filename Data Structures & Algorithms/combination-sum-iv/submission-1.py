class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        nums.sort()
        for i in range(1,target+1):
            for num in nums:
                if i < num:
                    break
                dp[i] += dp[i - num]
        
        return dp[target]
                