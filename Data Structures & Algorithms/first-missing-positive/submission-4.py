class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = [i for i in range(1,len(nums) + 2)]
        checkset = set(missing)

        for num in nums:
            if num in checkset:
                checkset.remove(num)
        return min(checkset)