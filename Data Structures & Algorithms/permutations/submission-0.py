class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        returnList = []

        def permuteRecurse(nums: List[int], output: List[int]) -> None:
            if len(output) == len(nums):
                returnList.append(output[:])
                return

            print(output)

            for num in nums:
                if num in output:
                    continue
                output.append(num)
                permuteRecurse(nums, output)
                output.pop()

        permuteRecurse(nums, [])

        return returnList
                

