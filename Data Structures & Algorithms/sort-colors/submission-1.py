class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        ptr = 0

        while ptr <= j:
            if nums[ptr] == 0:
                temp = nums[ptr]
                nums[ptr] = nums[i]
                nums[i] = temp
                ptr += 1
                i += 1
            elif nums[ptr] == 1:
                ptr += 1
            elif nums[ptr] == 2:                
                temp = nums[ptr]
                nums[ptr] = nums[j]
                nums[j] = temp
                j -= 1
        