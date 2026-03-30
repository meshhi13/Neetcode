class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowI = 0
        colI = 0
        rowJ = len(matrix) - 1
        colJ = len(matrix[0]) - 1

        row = 0
        col = 0  
        while rowI <= rowJ:
            row = (rowJ + rowI) // 2
            print(row, matrix[row])

            
            if matrix[row][0] <= target and matrix[row][len(matrix[0]) - 1] >= target:
                break

            if matrix[row][0] > target:
                rowJ = row - 1
            
            if matrix[row][len(matrix[0]) - 1] < target:
                rowI = row + 1

        while colI <= colJ:
            print(row, col, matrix[row][col])
            col = (colI + colJ) // 2

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                colJ = col - 1

            if matrix[row][col] < target:
                colI = col + 1


        return False