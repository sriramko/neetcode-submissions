class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prevmax = nums[0]
        globalmax = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            if prevmax < 0:
                prevmax = curr
            else:
                prevmax += curr
            if (prevmax > globalmax):
                globalmax = prevmax
        return globalmax