class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = ["JFK"]
        adjList = collections.defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            adjList[src].append(dest)
        #create adjacency list in sorted order

        def dfs(node) -> bool:
            if len(itinerary) == len(tickets) + 1:
                return True
            if node not in adjList:
                return False
            
            temp = list(adjList[node])
            for i, n in enumerate(temp):
                adjList[node].pop(i)
                itinerary.append(n)
                if dfs(n): return True
                adjList[node].insert(i, n)
                itinerary.pop()
            return False

        dfs("JFK")
        return itinerary