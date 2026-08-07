class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num0 = 0
        for num in nums:
            if num == 0:
                num0 += 1
            else:
                product *= num
        res = [0] * len(nums)
        if num0 > 1:
            return res
        elif num0 == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product
                    return res
        else:
            for i in range(len(nums)):
                res[i] = int(product / nums[i])
            return res