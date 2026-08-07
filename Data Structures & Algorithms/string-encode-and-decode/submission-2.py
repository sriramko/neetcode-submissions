class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        l = 0
        r = 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            num = int(s[l:r])
            res.append(s[r+1:r+num+1])
            l = r = r + num + 1
        return res


