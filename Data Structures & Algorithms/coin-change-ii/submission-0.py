class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1 for _ in coins] for _ in range(amount + 1)]

        def coinChangeRec(amount: int, index: int) -> int:
            current = 0
            if amount == 0:
                return 1

            if amount < 0:
                return 0

            if index >= len(coins):
                return 0

            if memo[amount][index] != -1:
                return memo[amount][index]
            
            current += coinChangeRec(amount - coins[index], index)
            current += coinChangeRec(amount, index + 1)

            memo[amount][index] = current

            return memo[amount][index]

        return coinChangeRec(amount, 0)
