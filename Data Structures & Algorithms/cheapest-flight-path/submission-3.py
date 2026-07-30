class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_map = {flight[0]: [] for flight in flights}

        for flight in flights:
            adj_map[flight[0]].append((flight[1], flight[2]))

        dp = [[-1 for _ in range(0, n)] for _ in range(0, k + 2)]

        def dfs(start: int, stops: int) -> int:
            if dp[stops][start] != -1:
                return dp[stops][start]

            if start == dst:
                dp[stops][start] = 0
                return 0

            if stops == 0:
                dp[stops][start] = math.inf
                return dp[stops][start]

            cost = math.inf

            for neighbor, price in adj_map.get(start, []):
                cost = min(cost, price + dfs(neighbor, stops - 1))

            dp[stops][start] = cost
            return cost

        res = dfs(src, k + 1)
        if res == math.inf:
            return -1
        else:
            return res  