class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        l, r = 0, 0
        longest = 0
        while r < len(s):
            if s[r] not in contains:
                contains.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                while s[r] in contains:
                    contains.remove(s[l])
                    l += 1
        return longest