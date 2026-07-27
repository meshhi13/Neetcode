class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1 for _ in prices] for _ in (True, False)]

        def dfs(index, bought):
            if index >= len(prices):
                return 0

            if memo[bought][index] != -1:
                return memo[bought][index]

            res = dfs(index + 1, bought)

            if bought == 1:
                res = max(res, prices[index] + dfs(index + 2, 0))
            else:
                res = max(res, -prices[index] + dfs(index + 1, 1))

            memo[bought][index] = res
            return res

        return dfs(0, 0)
            

