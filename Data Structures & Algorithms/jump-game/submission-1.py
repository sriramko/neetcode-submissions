class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        bound = 0
        for i in range(0, end+1):
            if i <= bound:
                bound = max(bound, i + nums[i])
        
        return (bound >= end)
        
            