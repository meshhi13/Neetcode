class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[math.inf for _ in range(len(word2))] for _ in range(len(word1))]
        def minDistanceRec(word1: str, word2: str) -> int:
            if not word1:
                return len(word2)
    
            if not word2:
                return len(word1)

            if dp[len(word1) - 1][len(word2) - 1] != math.inf:
                return dp[len(word1) - 1][len(word2) - 1]
    
            if word1[0] == word2[0]:
                dp[len(word1) - 1][len(word2) - 1] = minDistanceRec(word1[1:], word2[1:])
                return dp[len(word1) - 1][len(word2) - 1]

            dp[len(word1) - 1][len(word2) - 1] = min(1 + minDistanceRec(word1[1:], word2), 1 + minDistanceRec(word1, word2[1:]), 1 + minDistanceRec(word1[1:], word2[1:]))

            return dp[len(word1) - 1][len(word2) - 1]

        for i in dp:
            print(i)
        return minDistanceRec(word1, word2)

        