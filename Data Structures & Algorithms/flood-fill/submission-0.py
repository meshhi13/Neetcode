class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initColor = image[sr][sc]

        queue = []
        queue.append((sr, sc))

        while queue:
            cur = queue.pop()
            i = cur[0]
            j = cur[1]

            if image[i][j] == initColor and image[i][j] != color:
                image[i][j] = color
                if i > 0:
                    queue.append((i - 1, j))
                if i < len(image) - 1:
                    queue.append((i + 1, j))
                if j > 0:
                    queue.append((i, j - 1))
                if j < len(image[0]) - 1:
                    queue.append((i, j + 1))

        return image