class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record = 0
        for num in nums:
            record ^= num

        return record