class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = [0, 0, 0, 0]
        length = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        def backtrack(sticks) -> bool:
            if not sticks:
                return True
            stick = sticks[0]
            for i in range(4):
                if side[i] + stick > length:
                    continue
                side[i] += stick
                if backtrack(sticks[1:]):
                    return True
                side[i] -= stick
            return False
        return backtrack(matchsticks)