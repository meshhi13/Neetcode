class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = sum(range(0, len(nums) + 1))
        for i in nums:
            cur -= i

        return cur