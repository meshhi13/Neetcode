import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        boardCopy = copy.deepcopy(board)

        def dfs(x, y):
            queue = []
            queue.append((x, y))
            visited = set()

            while queue:
                i, j = queue.pop()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                boardCopy[i][j] = "X"
                
                if i > 0:
                    if board[i - 1][j] == "O":
                        queue.append((i - 1, j))
                if i < len(board) - 1:
                    if board[i + 1][j] == "O":
                        queue.append((i + 1, j))
                if j > 0:
                    if board[i][j - 1] == "O":
                        queue.append((i, j - 1))
                if j < len(board[0]) - 1:
                    if board[i][j + 1] == "O":
                        queue.append((i, j + 1))


        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                dfs(i, len(board[0]) - 1)
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0, i)
            if board[len(board) - 1][i] == "O":
                dfs(len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and boardCopy[i][j] == "O":
                    board[i][j] = "X"

        