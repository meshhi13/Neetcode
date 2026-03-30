class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        if l > r:
            return -1
        
        mid = l + (r - l) // 2
        midNum = nums[mid]

        if midNum == target:
            return mid
        
        if midNum > target:
            return self.binary_search(nums, l, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, r, target)

        