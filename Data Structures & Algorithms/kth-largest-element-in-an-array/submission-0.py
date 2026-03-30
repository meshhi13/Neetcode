import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for i in range(len(nums) - k):
            item = heapq.heappop(nums)
            print(i, item)

        return heapq.heappop(nums)