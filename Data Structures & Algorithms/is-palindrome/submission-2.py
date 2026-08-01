class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        alphanumeric = set([                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"
            ])
        
        for i in s:
            if i in alphanumeric:
                res += i

        

        return res[::-1] == res
        