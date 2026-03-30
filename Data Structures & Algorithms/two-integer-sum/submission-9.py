class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for n, i in enumerate(nums):
            if target - i in hashMap:
                return [hashMap[target - i], n]
            else:
                hashMap[i] = n

