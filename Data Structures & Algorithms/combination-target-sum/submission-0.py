class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(nums, target, output):
            if target < 0:
                return

            if target == 0:
                result.append(output[:])
                return

            for i in range(len(nums)):
                output.append(nums[i])
                backtrack(nums[i:], target - nums[i], output)
                output.pop()

        
        backtrack(nums, target, []) 
        return result

            

            

            

