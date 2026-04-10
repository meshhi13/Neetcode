class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        global memo 
        memo = [[0 for _ in range(n)] for _ in range(m)] 
        i = m - 1
        j = n - 1
        memo[i][j] = 1
        j -= 1

        while i >= 0:
            while j >= 0:
                bottom = 0
                right = 0
                if i + 1 < m:
                    bottom = memo[i + 1][j]
                if j + 1 < n:
                    right = memo[i][j + 1]

                memo[i][j] = bottom + right

                j -= 1

            i -= 1
            j = n - 1

        return memo[0][0]



                