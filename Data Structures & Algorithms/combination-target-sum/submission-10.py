class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(cur, i, remain):
            if i == len(nums) or remain < 0:
                return
            if remain == 0:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(cur, i, remain - nums[i])
            cur.pop()
            backtrack(cur, i+1, remain)

        backtrack([], 0, target)
        return res