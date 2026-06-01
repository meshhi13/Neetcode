class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            contains = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in contains:
                        return False
                    else:
                        contains.add(board[i][j])

        for i in range(len(board[0])):
            contains = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in contains:
                        return False
                    else:
                        contains.add(board[j][i])
        
        for i in range(3):
            for j in range(3):
                contains = set()
                for x in range(3*i, 3*i + 3):
                    for y in range(3*j, 3*j + 3):
                        if board[x][y] == ".":
                            continue
                        else:
                            if board[x][y] in contains:
                                return False
                            else:
                                contains.add(board[x][y])

        return True