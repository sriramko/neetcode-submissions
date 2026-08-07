class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        lookup = [0,1,1] + [0] * (n - 2)
        for i in range(3,n+1):
            lookup[i] = lookup[i-1] + lookup[i-2] + lookup[i-3]
        return lookup[n] 