class Solution:
    def climbStairs(self, n: int) -> int:
        dptable = []
        dptable.append(1)
        dptable.append(2)
        for i in range(2,n):
            dptable.append(dptable[i-1]+dptable[i-2])
        return dptable[n-1]