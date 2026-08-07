class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(len(s), i + maxJump + 1)):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        
        return False

        