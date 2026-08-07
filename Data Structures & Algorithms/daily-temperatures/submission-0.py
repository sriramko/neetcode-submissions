class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        if len(res) == 1:
            return res
        stack = []
        ptr = 0
        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                res[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, temp])
        return res
        