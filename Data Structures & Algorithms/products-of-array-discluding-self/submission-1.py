class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [0] * length
        suf = [0] * length
        res = [0] * length
        pre[0] = 1
        suf[length - 1] = 1
        for i in range(1,length):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(length-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(length):
            res[i] = pre[i] * suf[i]
        return res
        