class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        pos = 0
        while pos < len(triplets):
            candidate = triplets[pos]
            test = [max(target[0],candidate[0]),max(target[1],candidate[1]),max(target[2],candidate[2])]
            if test != target:
                triplets.pop(pos)
                continue
            pos += 1
            for i in range(3):
                if candidate[i] == target[i]:
                    found[i] = True
        return found[0] and found[1] and found[2]

