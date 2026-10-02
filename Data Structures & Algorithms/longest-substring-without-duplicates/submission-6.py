class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            longest = max(longest, r - l + 1)
        return longest