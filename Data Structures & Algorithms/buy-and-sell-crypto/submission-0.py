class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxSell = 0

        for i in prices:
            minBuy = min(minBuy, i)
            maxSell = max(maxSell, i - minBuy)

        return maxSell
            