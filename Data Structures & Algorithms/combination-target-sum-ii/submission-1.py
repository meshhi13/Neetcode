class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(nums, target, output):
            if target < 0:
                return

            if target == 0:
                result.append(output[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                output.append(nums[i])
                backtrack(nums[i + 1:], target - nums[i], output)
                output.pop()

        
        backtrack(candidates, target, []) 
        return result

            

            

            

