class Solution:
    def DFS(self, i: int, j: int, grid: List[List[int]]) -> List[List[int]]:
        queue = []
        queue.append((i, j))
        grid[i][j] = 0
        count = 0
        while queue:
            coor = queue.pop()
            i = coor[0] 
            j = coor[1]
            count += 1
            if i - 1 >= 0:
                if grid[i-1][j] == 1:
                    queue.append((i-1, j))
                    grid[i-1][j] = 0
            if j - 1 >= 0:
                if grid[i][j-1] == 1:
                    queue.append((i, j-1))
                    grid[i][j-1] = 0
            if i + 1 < len(grid):
                if grid[i+1][j] == 1:
                    queue.append((i+1, j))
                    grid[i+1][j] = 0
            if j + 1 < len(grid[0]):
                if grid[i][j+1] == 1:
                    queue.append((i, j + 1))
                    grid[i][j+1] = 0

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(self.DFS(i, j, grid), maxArea)

        return maxArea