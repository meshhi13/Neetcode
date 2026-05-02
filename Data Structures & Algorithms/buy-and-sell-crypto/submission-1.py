class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        lowestValue = prices[0]

        for i in prices:
            lowestValue = min(lowestValue, i)
            maxProfit = max(maxProfit, i - lowestValue)

        return maxProfit