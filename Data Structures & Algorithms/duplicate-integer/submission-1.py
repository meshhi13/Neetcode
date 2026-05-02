class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        for i, j in hashMap.items():
            if j > 1:
                return True

        return False