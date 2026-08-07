class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    curSum = num
            return subarray <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res