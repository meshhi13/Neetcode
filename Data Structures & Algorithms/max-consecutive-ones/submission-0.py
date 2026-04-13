class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0
        for i in nums:
            if i == 1:
                currOnes += 1
            else:
                currOnes = 0
            
            maxOnes = max(currOnes, maxOnes)

        return maxOnes