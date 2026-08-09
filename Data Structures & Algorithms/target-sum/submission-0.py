class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = [{} for _ in nums]

        def findTargetRec(amount: int, index: int) -> int:
            if amount == target and index == len(nums):
                return 1

            if index >= len(nums):
                return 0
            
            if amount in memo[index]:
                return memo[index][amount]

            current = 0

            current += findTargetRec(amount + nums[index], index + 1)
            current += findTargetRec(amount - nums[index], index + 1)

            memo[index][amount] = current
            return current

        return findTargetRec(0, 0)