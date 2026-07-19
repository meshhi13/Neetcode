class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        result = []

        for i in range(0, len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while j < k:
                if nums[i] + nums[k] + nums[j] == 0:
                    if j <= i + 1 or nums[j] != nums[j - 1]:
                        result.append([nums[i], nums[k], nums[j]])
                    j += 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    j += 1
                else:
                    k -= 1           

        return result
            
        