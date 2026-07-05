class KthLargest:
    heq = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.heq = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heq, val)
        while len(self.heq) > self.k:
            heapq.heappop(self.heq)

        return self.heq[0]

