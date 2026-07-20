class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxGlobal = nums[0]
        currentMin = nums[0]
        currentMax = nums[0]

        for i in range(1, len(nums)):
            prevMax = currentMax
            currentMax = max(nums[i], nums[i] * currentMax, nums[i] * currentMin)
            currentMin = min(nums[i], nums[i] * currentMin, nums[i] * prevMax)
            maxGlobal = max(maxGlobal, currentMax)

        return maxGlobal


        # maxProduct = nums[0]

        # for i in range(len(nums)):
        #     current = nums[i]
        #     maxProduct = max(current, maxProduct)
        #     for j in range(i + 1, len(nums)):
        #         current *= nums[j]
        #         maxProduct = max(current, maxProduct)
        #         if nums[j] == 0:
        #             break

        # return maxProduct



        


        