class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in complements:
                return [complements[diff], i]
            complements[n] = i
        return

            
        