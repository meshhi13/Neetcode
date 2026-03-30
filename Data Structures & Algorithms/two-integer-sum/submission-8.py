class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                if (nums.index(target - nums[i], i+1, len(nums)) != -1):
                    return [i, nums.index(target - nums[i], i+1, len(nums))]
            except:
                pass