class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1 for _ in prices] for _ in (True, False)]

        def dfs(index, bought):
            if index == len(prices):
                return 0

            if memo[1 if bought else 0][index] != -1:
                return memo[1 if bought else 0][index]

            res = dfs(index + 1, bought)

            if bought:
                res = max(res, prices[index] + dfs(index + 1, False))
            else:
                res = max(res, -prices[index] + dfs(index + 1, True))

            memo[1 if bought else 0][index] = res
            return res
        
        return dfs(0, False)