class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for num in nums:
            new = set()
            for subarray in dp:
                if subarray + num == target:
                    return True
                if subarray + num > target:
                    continue
                else:
                    new.add(subarray + num)
            dp.update(new)
        return False