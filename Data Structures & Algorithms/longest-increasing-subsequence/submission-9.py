class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1 for _ in nums]
        memo[0] = 1

        def dfs(end):
            # dfs[n] = 1 + max(dfs[k] | k < n, nums[k] < nums[n))
            max_res = 0

            if memo[end] != -1:
                return memo[end]
            
            for index in range(0, end):
                if nums[end] > nums[index]:
                    max_res = max(max_res, dfs(index))

            memo[end] = max_res + 1
            return memo[end]

        
        for index in range(0, len(nums)):
            dfs(index)

        return max(memo)