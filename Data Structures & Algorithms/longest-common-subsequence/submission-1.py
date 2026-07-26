class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in text2] for _ in text1]

        memo[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, len(memo)):
            if text1[i] == text2[0]:
                memo[i][0] = 1
            else:
                memo[i][0] = max(memo[i - 1][0], memo[0][0])

        for j in range(1, len(memo[0])):
            if text2[j] == text1[0]:
                memo[0][j] = 1
            else:
                memo[0][j] = max(memo[0][j - 1], memo[0][0])

        for i in range(1, len(memo)):
            for j in range(1, len(memo[0])):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        return memo[-1][-1]




        