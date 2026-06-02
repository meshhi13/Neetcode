class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def backtrack(nums):
            if not nums:
                return

            res = []
            for i in result:
                copy = list(i)
                copy.append(nums[0])
                print(copy)
                res.append(copy)

            result.extend(res)
            backtrack(nums[1:])

        backtrack(nums)
        return result