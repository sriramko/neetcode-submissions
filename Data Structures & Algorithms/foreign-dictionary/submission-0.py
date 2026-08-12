class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { char : set() for w in words for char in w }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} #False=visited, True=visited + In current path
        res = []

        def dfs(char: str) -> bool:
            if char in visit:
                return visit[char]
            else:
                visit[char] = True
            for after in adj[char]:
                if dfs(after):
                    return True
            visit[char] = False
            res.append(char)
            return False

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)