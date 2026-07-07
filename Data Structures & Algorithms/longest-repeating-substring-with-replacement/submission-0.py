class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hMap = {}
        mostFreq = None
        maxF = 0
    
        l = 0
    
        for r in range(len(s)):
            hMap[s[r]] = 1 + hMap.get(s[r], 0)
            maxF = max(maxF, hMap[s[r]])
            while (r - l + 1) -  maxF > k:
                hMap[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result



        