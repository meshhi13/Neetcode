class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) 

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue
            else:
                heapq.heappush_max(stones, x - y)

        return 0 if not stones else stones[0]