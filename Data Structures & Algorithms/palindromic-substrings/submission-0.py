class Solution:
    def countSubstrings(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            #odd lengths first
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                number += 1
                l -= 1
                r += 1
        for i in range(len(s) - 1):
            #even lengths next
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                number += 1
                l -= 1
                r += 1
        return number