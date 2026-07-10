class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            q = []
            q.append(node)

            while q:
                cur = q.pop(0)
                neighbors = adjList.get(cur, [])

                if cur in found:
                    continue

                found.add(cur)

                for i in neighbors:
                    q.append(i)

        adjList = {}
        found = set()

        for i in edges:
            adjList[i[0]] = adjList.get(i[0], [])
            adjList[i[0]].append(i[1])
            adjList[i[1]] = adjList.get(i[1], [])
            adjList[i[1]].append(i[0])

        count = 0

        for i in range(n):
            if i in found:
                continue
                
            dfs(i)
            count += 1

        return count

        
            

            


