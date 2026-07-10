from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]):

        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                continue

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)

        return len(visited) == n