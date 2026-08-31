class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = [i + 1 for i in range(len(nums) + 1)]
        checkset = set(missing)

        for num in nums:
            if num in checkset:
                checkset.remove(num)
        return min(checkset)