class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        curr = []
        def backtrack(i):
            if i == len(nums) or sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i)
            curr.pop()
            backtrack(i+1)

        backtrack(0)
        return res