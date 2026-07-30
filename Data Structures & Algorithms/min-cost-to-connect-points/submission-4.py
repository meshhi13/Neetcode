class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # min spanning tree where weight is manahattan distance from point to point
        adj_matrix = [[0 for _ in points] for _ in points]
        for i in range(len(points)):
            for j in range(len(points)):
                adj_matrix[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visited = set([0])

        pq = [(adj_matrix[0][j], j) for j in range(len(adj_matrix[0])) if j != 0]

        heapq.heapify(pq)

        total = 0

        while pq:
            cost, cur = heapq.heappop(pq)
            if cur in visited:
                continue

            visited.add(cur)
            total += cost

            for point in [(adj_matrix[cur][j], j) for j in range(len(adj_matrix[cur])) if j != cur]:
                heapq.heappush(pq, point)

        return total
