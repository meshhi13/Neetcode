class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        results = [[math.inf for _ in grid[0]] for _ in grid]

        pq = [(grid[0][0], 0, 0)]
        max_elev = grid[0][0]
        seen = set((0, 0))
        while pq:
            elev, x, y = heapq.heappop(pq)

            max_elev = max(elev, max_elev)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return max_elev
            
            if (x, y) in seen:
                continue

            seen.add((x, y))

            if x > 0:
                heapq.heappush(pq, (grid[x - 1][y], x - 1, y))
            if x < len(grid) - 1:
                heapq.heappush(pq, (grid[x + 1][y], x + 1, y))
            if y > 0:
                heapq.heappush(pq, (grid[x][y - 1], x, y - 1))
            if y < len(grid[0]) - 1:
                heapq.heappush(pq, (grid[x][y + 1], x, y + 1))

        


