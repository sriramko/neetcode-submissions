class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        #two queues with relative indexes

        while D and R:
            Dturn = D.popleft()
            Rturn = R.popleft()

            if Rturn < Dturn:
                R.append(Dturn + len(senate))
            else:
                D.append(Rturn + len(senate))

        return "Radiant" if R else "Dire"