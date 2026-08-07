class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        return min(nums)
        # length = len(nums)
        # l = 0
        # r = length - 1
        # m = (l + r) // 2
        # while l <= r:
        #     if nums[m] == target:
        #         return m
        #     elif target > nums[m]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        #     m = (l + r) // 2
        # return -1