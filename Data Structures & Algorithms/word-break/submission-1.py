class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None for _ in range(len(s) + 1)]

        def recSolve(i: int) -> bool:
            if memo[i] != None:
                return memo[i]

            if i == len(s):
                memo[i] = True
                return memo[i]
            
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                
                if s[i: i + len(word)] == word:
                    memo[i] = recSolve(i + len(word))
                    if memo[i] == True:
                        return memo[i]

            memo[i] = False
            return memo[i]

        return recSolve(0)