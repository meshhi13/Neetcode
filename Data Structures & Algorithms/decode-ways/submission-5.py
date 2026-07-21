class Solution:
    def numDecodings(self, s: str) -> int:
        hashM = {}

        def dfs(s):
            if not s:
                return 1

            if s in hashM:
                return hashM[s]
            
            if s[0] == '0':
                return 0

            if len(s) > 1 and (s[0] == '1' or (s[0] == '2' and int(s[1]) < 7)):
                hashM[s] = dfs(s[1:]) + dfs(s[2:])
                return hashM[s]
            else:
                hashM[s] = dfs(s[1:])
                return hashM[s]

        return dfs(s)

            
        


        
