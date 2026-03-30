class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS, stringT = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            stringS[s[i]] = stringS.get(s[i], 0) + 1
            stringT[t[i]] = stringT.get(t[i], 0) + 1
        
        for i in stringS:
            if stringS[i] != stringT.get(i):
                return False

        return True
        