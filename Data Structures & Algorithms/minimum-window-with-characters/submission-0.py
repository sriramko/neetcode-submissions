from collections import Counter

class Solution:
    def contains(self, dicts, dictt):
        # check required keys
        if dictt.keys() - dicts.keys():
            return False
        
        # check frequencies
        for key in dictt:
            if dicts[key] < dictt[key]:     # FIXED
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        lent = len(t)
        lens = len(s)
        if lent == 0 or lent > lens:
            return ""

        l = 0
        r = lent
        currbest = ""
        dictt = Counter(t)

        while r <= lens + 1:
            currstring = s[l:r]
            dicts = Counter(currstring)
            
            # FIXED LOGIC
            if self.contains(dicts, dictt):
                if len(currbest) == 0 or len(currstring) < len(currbest):
                    currbest = currstring
                l += 1
            else:
                r += 1
        
        return currbest
