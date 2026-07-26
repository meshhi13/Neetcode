class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[False for _ in s] for _ in s]

        total = 0
        for i in range(0, len(s))[::-1]:
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or memo[i + 1][j - 1]:
                        memo[i][j] = True
                        total += 1

        return total

        