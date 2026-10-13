class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return False
            if total == target:
                return True
            return dfs(i+1, total + nums[i]) or dfs(i+1, total)
        
        return dfs(0,0)