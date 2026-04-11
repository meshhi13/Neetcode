class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -math.inf
        curr = 0 

        for i in nums:
            curr += i
            maxi = max(curr, maxi)

            if curr < 0:
                curr = 0

        return maxi