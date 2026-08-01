class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def find(node: int):
            if node != res[node]:
                res[node] = find(res[node])

            return res[node]

        def union(node1: int, node2: int) -> bool:
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False

            if rank[parent1] > rank[parent2]:
                res[parent2] = parent1
                rank[parent1] += rank[parent2]
                
            else:
                res[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]