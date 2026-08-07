class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            alpha = tuple(sorted(string))
            if alpha in hashmap:
                hashmap[alpha].append(string)
            else:
                hashmap[alpha] = [string]
        out = []
        for sublist in hashmap.values():
            out.append(sublist)
        return out


        