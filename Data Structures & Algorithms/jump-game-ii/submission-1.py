class Solution:
    def jump(self, nums: List[int]) -> int:
        numJumps = 0
        left = right = 0
        while (right < len(nums) - 1):
            next = right
            for i in range(left, right + 1):
                next = max(next, i+nums[i])
            left = right + 1
            right = next
            numJumps += 1
        
        return numJumps