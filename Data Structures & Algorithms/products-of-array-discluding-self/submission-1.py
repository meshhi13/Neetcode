class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = []
        left_total = 1
        right_side = []
        right_total = 1
        
        finals = []
        for index in range(len(nums)):
            left_total *= nums[index]
            left_side.append(left_total)

            right_total *= nums[len(nums) - index - 1]
            right_side.append(right_total)

        right_side.reverse()

        for index in range(len(nums)):
            current = 0
            if index == 0:
                current = right_side[index + 1]
            elif index == len(nums) - 1:
                current = left_side[index - 1]
            else:
                current = left_side[index - 1] * right_side[index + 1]

            finals.append(current)

        return finals