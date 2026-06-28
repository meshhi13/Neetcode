class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        def backtrack(nums: List[int], path: List[int] = [], index: int = 0) -> None:
            if index == len(nums):
                output.append(path[:])
                return

            path.append(nums[index])
            backtrack(nums, path, index + 1)
            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtrack(nums, path, index + 1)

        backtrack(nums) 

        return output

            