"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {} #hashmap from original node to deep copy

        def bfs(original):
            if original in clones:
                return clones[original]
            clone = Node(original.val)
            clones[original] = clone
            for nei in original.neighbors:
                clone.neighbors.append(bfs(nei))
            return clone


        return bfs(node)
