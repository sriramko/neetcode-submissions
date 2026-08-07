class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currlength = len(nums)
        i = 0
        while i < currlength:
            if nums[i] == val:
                del nums[i]
                currlength -= 1
            else:
                i += 1
        return currlength