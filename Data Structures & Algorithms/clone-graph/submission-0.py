"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    added = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        if node in self.added:
            return self.added[node]

        clone = Node(node.val)
        self.added[node] = clone

        for i in node.neighbors:
            clone.neighbors.append(self.cloneGraph(i))

        return clone