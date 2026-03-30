class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currset = set()
        maxLen = 0
        i = 0
        j = 0
        while j < len(s):
            while s[j] in currset:
                currset.remove(s[i])
                i += 1
            
            currset.add(s[j])
            maxLen = max(j - i + 1, maxLen)
            j += 1

        return maxLen
