class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        attempt = [0,0,0]
        for triplet in triplets:
            if max(attempt[0], triplet[0]) > target[0] or max(attempt[1], triplet[1]) > target[1] or max(attempt[2], triplet[2]) > target[2]:
                continue
            attempt[0] = max(attempt[0],triplet[0])
            attempt[1] = max(attempt[1],triplet[1])
            attempt[2] = max(attempt[2],triplet[2])
        return attempt == target