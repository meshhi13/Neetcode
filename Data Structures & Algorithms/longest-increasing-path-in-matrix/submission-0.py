class Solution:
    def graphify(self, grid):
        graph = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                neighbors = []
                if i + 1 < len(grid):
                    if grid[i][j] > grid[i + 1][j]:
                        neighbors.append((i + 1, j))
                if i - 1 >= 0:
                    if grid[i][j] > grid[i - 1][j]:
                        neighbors.append((i - 1, j))
                if j + 1 < len(grid[0]):
                    if grid[i][j] > grid[i][j + 1]:
                        neighbors.append((i, j + 1))
                if j - 1 >= 0:
                    if grid[i][j] > grid[i][j - 1]:
                        neighbors.append((i, j - 1))
    
                graph[(i, j)] = neighbors
    
        return graph
    
    def recSolve(self, coor, graph):
        if graph[coor] == []:
            return 1
        
        if memo[coor[0]][coor[1]] != -1:
            return memo[coor[0]][coor[1]]
    
        maxDist = 0
        for i in graph[coor]:
            currDistance = self.recSolve(i, graph)
            maxDist = max(currDistance, maxDist)
            if memo[i[0]][i[1]] < currDistance:
                memo[i[0]][i[1]] = currDistance 
            
        return 1 + maxDist        
    
    def longestIncreasingPath(self, grid):
        global memo 
        memo = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        graph = self.graphify(grid)
        for coor in graph.keys():
            memo[coor[0]][coor[1]] = self.recSolve(coor, graph)
    
        maxRes = 0
        for i in memo:
            for j in i:
                maxRes = max(maxRes, j)
        
        return maxRes