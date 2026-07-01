class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0

        while i < len(nums) - 1:
            maxJump = nums[i]
            netDist = 1
            whereTo = i + 1
            
            for j in range(i + 1, min(len(nums), i + maxJump + 1)):
                if nums[j] + j >= len(nums) - 1:
                    whereTo = j
                if nums[j] + j >= netDist:
                    whereTo = j
                    netDist = nums[j] + j

            print(i)
            i = whereTo
            count += 1

        return count 