class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                register[0] += 1
                continue
            if bill == 10:
                if register[0] == 0:
                    return False
                register[0] -= 1
                register[1] += 1
                continue
            else:
                if register[1] > 0 and register[0] > 0:
                    register[1] -= 1
                    register[0] -= 1
                    register[2] += 1
                    continue
                elif register[0] >= 3:
                    register[0] -= 3
                    register[2] += 1
                    continue
                else:
                    return False

        return True