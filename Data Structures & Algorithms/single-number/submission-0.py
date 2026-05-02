class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = 0
        for i in nums:
            start ^= i

        return start