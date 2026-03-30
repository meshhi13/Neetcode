class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = nums[j] + nums[k] + nums[i]
                if result == 0:
                    lis = [nums[j], nums[i], nums[k]]
                    lis.sort()
                    solutions.add(tuple(lis))
                    k = k - 1

                if result < 0:
                    j = j + 1
                if result > 0:
                    k = k - 1

        return list(solutions)
            
        