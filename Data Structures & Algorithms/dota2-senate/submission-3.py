class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        turn = len(senate)

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            if c == "D":
                D.append(i)
        
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + turn)
            else:
                D.append(d + turn)
        return "Radiant" if R else "Dire"
