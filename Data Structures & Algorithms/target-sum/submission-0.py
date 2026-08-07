class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def backtrack(i, cursum):
            if i == n:
                return 1 if cursum == target else 0
            return backtrack(i + 1, cursum + nums[i]) + backtrack(i + 1, cursum - nums[i])
        
        return backtrack(0,0)