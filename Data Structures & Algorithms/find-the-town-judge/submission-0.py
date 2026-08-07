class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustThem = [0] * n
        theyTrust = [0] * n
        for a, b in trust:
            trustThem[b-1] += 1
            theyTrust[a-1] += 1
        for i in range(n):
            if trustThem[i] == n - 1 and theyTrust[i] == 0:
                return i + 1
        return -1