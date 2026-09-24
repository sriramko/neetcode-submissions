class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window size
        if len(s1) > len(s2):
            return False
        Count = [0] * 26

        for i in range(len(s1)):
            Count[ord(s1[i]) - ord('a')] += 1
            Count[ord(s2[i]) - ord('a')] -= 1
        
        for r in range(len(s1),len(s2)):
            if not any(Count):
                return True
            Count[ord(s2[r]) - ord('a')] -= 1
            Count[ord(s2[r-len(s1)]) - ord('a')] += 1
        return not any(Count)