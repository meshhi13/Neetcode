class Solution:
    def reverseBits(self, n: int) -> int:
        r = bin(n)[2:].zfill(32)
        r = r[::-1]
        return int(r, 2)
        return 0