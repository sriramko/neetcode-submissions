class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n
        emails = defaultdict(int) # email to account index
    
        def find(account: int) -> int:
            res = account
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(a1: int, a2: int) -> int:
            p1, p2 = find(a1), find(a2)
            if p1 == p2:
                return 1
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 0
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emails:
                    union(i,emails[e])
                else:
                    emails[e] = i
        
        emailGroup = defaultdict(list) # index of acc -> list of emails
        for e, i in emails.items():
            leader = find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res