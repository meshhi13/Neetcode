class Solution:

    def rob(self, nums: List[int]) -> int:
        self.memo = [-1] * (len(nums) + 1)
        return self.robRec(nums, 0)
        
    def robRec(self, nums, index):
        if not nums: 
            return 0
        if len(nums) <= 2:
            maximum = 0
            for i in nums:
                maximum = max(maximum, i)
            return maximum
        
        maxim = 0

        if self.memo[index + 2] != -1:
            solution2 = self.memo[index + 2]
        else: 
            solution2 = self.robRec(nums[2:], index + 2)
            self.memo[index + 2] = solution2

        if self.memo[index + 3] != -1:
            solution3 = self.memo[index + 3]
        else: 
            solution3 = self.robRec(nums[3:], index + 3)
            self.memo[index + 3] = solution3

        
        maxim = max(maxim, nums[0] + solution2)
        maxim = max(maxim, nums[1] + solution3)

        return maxim
