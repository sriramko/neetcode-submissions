class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0

        tribonacci = [0,1,1]

        for i in range(3, n + 1):
            tribonacci[i % 3] = tribonacci[(i-1) % 3] + tribonacci[(i - 2) % 3] + tribonacci[(i - 3) % 3]
        return tribonacci[n % 3]