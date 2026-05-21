class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        def bfs(i, j):
            count = 0
            queue = []
            queue.append((i, j, 0))
            while queue:
                ii, jj, dist = queue.pop(0)
                if (ii, jj) in visited or grid[ii][jj] == -1:
                    continue
                visited.add((ii, jj))
                if grid[ii][jj] == 0:
                    return dist
                if ii > 0: queue.append((ii - 1, jj, dist + 1))
                if ii < len(grid) - 1: queue.append((ii + 1, jj, dist + 1))
                if jj > 0: queue.append((ii, jj - 1, dist + 1))
                if jj < len(grid[0]) - 1: queue.append((ii, jj + 1, dist + 1))
            
            return 2147483647


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == -1:
                    continue
                visited.clear()
                grid[x][y] = bfs(x, y)