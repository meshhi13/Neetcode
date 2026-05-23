class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        def bfs(r, c):
            pacific = False
            atlantic = False
            queue = []
            queue.append((r, c))
            visited = set()
            while queue:
                x, y = queue.pop(0)
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if x == 0 or y == 0:
                    pacific = True
                if x == len(heights) - 1 or y == len(heights[0]) - 1:
                    atlantic = True

                if x > 0:
                    if heights[x - 1][y] <= heights[x][y]:
                        queue.append((x - 1, y))
                if y > 0:
                    if heights[x][y - 1] <= heights[x][y]:
                        queue.append((x, y - 1))
                if x < len(heights) - 1:
                    if heights[x + 1][y] <= heights[x][y]:
                        queue.append((x + 1, y))
                if y < len(heights[0]) - 1:
                    if heights[x][y + 1] <= heights[x][y]:
                        queue.append((x, y + 1))

            return pacific and atlantic

        returnList = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs(i, j):
                    returnList.append([i, j])

        return returnList