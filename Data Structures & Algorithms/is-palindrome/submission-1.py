class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz01234567890"

        res = ""
        for i in s:
            if i.lower() in letters:
                res += i.lower()
        
        for i in range(len(res) // 2):
            if res[i] == res[len(res) - 1 - i]:
                continue
            else:
                return False
        
        return True



