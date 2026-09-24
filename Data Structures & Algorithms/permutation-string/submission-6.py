class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False;
        l = 0
        r = len(s1)
        key = sorted(s1)
        while (r <= len(s2)):
            if (key == sorted(s2[l:r])):
                return True;
            l += 1
            r += 1
        return False;


