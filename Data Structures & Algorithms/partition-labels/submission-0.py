class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {} # last occurances
        for i, char in enumerate(s):
            last[char] = i
        start = end = 0
        res = []
        for i, char in enumerate(s):
            end = max(end,last[char])
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1    
        return res  
