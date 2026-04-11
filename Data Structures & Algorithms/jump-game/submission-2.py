class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        count = 0
        while i > 0:
            count += 1
            i -= 1
            if nums[i] >= count:
                count = 0

            print(i, count)

        if count == 0:
            return True
        else:
            return False

        