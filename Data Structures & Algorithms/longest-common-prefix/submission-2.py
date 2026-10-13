class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        longest = strs[0]
        for string in strs:
            for i in range(1,len(longest)+1):
                if longest[:i] != string[:i]:
                    longest = longest[:i-1]
                    break
        return longest