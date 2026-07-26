class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1 for _ in nums] for _ in nums]

        def dfs(i, j):
            if i == len(nums):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            LIS = dfs(i + 1, j)

            if nums[i] > nums[j] or j == -1:
                LIS = max(1 + dfs(i + 1, i), LIS)

            memo[i][j] = LIS
            return LIS

        return dfs(0, -1)
        