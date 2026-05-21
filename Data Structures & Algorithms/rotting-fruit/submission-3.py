class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        finalTime = 0
        while queue:
            x, y, time = queue.pop(0)
            finalTime = time

            if x > 0:
                if grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    queue.append((x - 1, y, time + 1))
            if x < len(grid) - 1:
                if grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    queue.append((x + 1, y, time + 1))
            if y > 0:
                if grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    queue.append((x, y - 1, time + 1))
            if y < len(grid[0]) - 1:
                if grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    queue.append((x, y + 1, time + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                    
        return finalTime


