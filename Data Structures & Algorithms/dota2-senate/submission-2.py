class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            elif c == "D":
                D.append(i)
        #two queues with relative indexes

        while D and R:
            Dturn = D.popleft()
            Rturn = R.popleft()

            if Rturn < Dturn:
                R.append(Rturn + len(senate))
            else:
                D.append(Dturn + len(senate))

        return "Radiant" if R else "Dire"