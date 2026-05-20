class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(xx, yy):
            print(xx, yy)
            queue = []
            queue.append((xx, yy))
            while len(queue) > 0:  
                x, y = queue.pop()
                grid[x][y] = "0"
                if x > 0:
                    if grid[x - 1][y] == "1":
                        queue.append((x - 1, y))
                if x < len(grid) - 1:
                    if grid[x + 1][y] == "1":
                        queue.append((x + 1, y))
                if y > 0:
                    if grid[x][y - 1] == "1":
                        queue.append((x, y - 1))
                if y < len(grid[0]) - 1:
                    if grid[x][y + 1] == "1":
                        queue.append((x, y + 1))

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    bfs(i, j)

        print(grid)
        return counter
