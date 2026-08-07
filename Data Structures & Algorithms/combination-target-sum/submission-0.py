class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(self, i: int, curr: List[int], curr_sum):
            if i >= len(nums):
                return
            curr_item = nums[i]
            for j in range(target - curr_sum//curr_item):
                if curr_sum + (j * curr_item) == target:
                    res.append(curr + [curr_item] * j)
                else:
                    after = curr + [curr_item] * j
                    dfs(self, i+1, after, curr_sum + curr_item*j)
        dfs(self, 0, [], 0)
        return res

        