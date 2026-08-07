class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 0
        for num in nums:
            if num == candidate:
                votes += 1
                continue
            else:
                votes -= 1
                if votes == 0:
                    candidate = num
                    votes = 1
        return candidate