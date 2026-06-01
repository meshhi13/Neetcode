class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(j):
            count = 0
            while j:
                count += j & 1
                j >>= 1
            
            return count

        res = []
        for i in range(0, n + 1):
            res.append(hammingWeight(i))

        return res