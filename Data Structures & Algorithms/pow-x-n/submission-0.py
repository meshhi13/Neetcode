class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = 1
        while n > 0:
            temp = temp * x
            n -= 1

        while n < 0:
            temp = temp / x
            n += 1

        return temp