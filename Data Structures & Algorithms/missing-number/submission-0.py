class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        record = 0
        for i in range(len(nums)+1):
            record ^= i
        for num in nums:
            record ^= num
        return record