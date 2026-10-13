class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
                continue
            count -= 1
            if count < 0:
                candidate = num
                count = 1
        return candidate