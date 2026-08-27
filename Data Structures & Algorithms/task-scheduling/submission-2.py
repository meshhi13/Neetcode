class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        time = 0

        counter = (list(counter.values()))
        counter = [-n for n in counter]
        heapq.heapify(counter)

        q = collections.deque()

        while counter or q:
            time += 1

            if q and q[0][1] <= time:
                new_count, old_time = q.popleft()

                if new_count < 0:
                    heapq.heappush(counter, new_count)

            if counter: 
                current = heapq.heappop(counter)
                if current == -1:
                    continue
                q.append((current + 1, time + n + 1))


        return time
