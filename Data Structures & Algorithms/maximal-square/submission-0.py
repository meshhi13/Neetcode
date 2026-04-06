class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = [[(0, 0, 0) for _ in matrix[0]] for _ in matrix]
        maxVal = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0:
                        memo[i][j] = 1
                    elif j == 0:
                        memo[i][j] = 1
                    else:
                        memo[i][j] = min(memo[i - 1][j], memo[i - 1][j - 1], memo[i][j - 1]) + 1
                else:
                    memo[i][j] = 0
                
                maxVal = max(maxVal, memo[i][j])

        return maxVal**2