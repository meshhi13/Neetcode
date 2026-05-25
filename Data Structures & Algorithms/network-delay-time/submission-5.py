class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = [(0, k)]
        seen = set()
        adj_list = {}
        max_so_far = 0

        for u, v, w in times:
            adj_list.setdefault(u, []).append((w, v))

        while pq:
            time, node = heapq.heappop(pq)

            if node in seen:
                continue

            seen.add(node)
            max_so_far = max(max_so_far, time)

            for weight, nei in adj_list.get(node, []):
                if nei not in seen:
                    heapq.heappush(pq, (time + weight, nei))

        return max_so_far if len(seen) == n else -1