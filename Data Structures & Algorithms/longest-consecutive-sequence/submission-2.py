class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lisMin = nums[0]
        lisMax = nums[0]

        for i in nums:
            lisMin = min(lisMin, i)
            lisMax = max(lisMax, i)
        
        diff = abs(lisMin - lisMax)

        newNums = [-1 for _ in range(diff + 1)]

        for i in nums:
            newNums[i - lisMin] = 1

        counter = 0
        maxCount = 0
        for i in newNums:
            if i != 1:
                counter = 0
            elif i == 1:
                counter += 1
                maxCount = max(maxCount, counter)

        return maxCount