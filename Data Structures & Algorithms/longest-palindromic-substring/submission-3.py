class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [[False for _ in s] for _ in s]

        maxLen = 0
        maxI = 0
        for i in range(0, len(s) - 1)[::-1]:
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or memo[i + 1][j - 1]:
                        memo[i][j] = True
                        if j - i >= maxLen:
                            maxLen = j - i
                            maxI = i
                
        return s[maxI: maxI + maxLen + 1]

        
        