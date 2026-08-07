class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i: int, curr: List[int], sum_so_far: int):
            if i == len(candidates):
                return
            curr_item = candidates[i]
            dfs(i+1, curr, sum_so_far)
            if curr_item + sum_so_far == target:
                solution = curr + [curr_item]
                res.add(tuple(solution))
            elif curr_item + sum_so_far < target:
                after = curr + [curr_item]
                dfs(i+1, after, sum_so_far + curr_item)

        dfs(0, [], 0)
        return [list(combination) for combination in res]