class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            mapper[nums[i]] = mapper.get(nums[i], 0) + 1

        mapper = dict(sorted(mapper.items(), key=lambda item: item[1]))

        result = list(mapper.keys())
        newResult = []
        for i in range(k):
           newResult.append(result.pop())

        return newResult