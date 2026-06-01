class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            contains1 = set()
            contains2 = set()
            for j in range(9):
                if board[i][j] == ".":
                    pass
                else:
                    if board[i][j] in contains1:
                        return False
                    else:
                        contains1.add(board[i][j])
                if board[j][i] == ".":
                    pass
                else:
                    if board[j][i] in contains2:
                        return False
                    else:
                        contains2.add(board[j][i])
        
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