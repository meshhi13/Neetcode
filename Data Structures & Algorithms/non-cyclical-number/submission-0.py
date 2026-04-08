class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        while n != 1:
            if hashMap.get(n, False):
                return False
            hashMap[n] = True

            acc = 0
            for i in list(str(n)):
                acc += (int(i)**2)
                print(i, acc)

            n = acc
        
        return True