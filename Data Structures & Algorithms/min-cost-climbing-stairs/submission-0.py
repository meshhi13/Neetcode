class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0 for _ in range(len(cost) + 1)]
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i - 2], memo[i - 1])

        memo[len(cost)] = min(memo[len(cost) - 2], memo[len(cost) - 1])

        return memo[-1]
