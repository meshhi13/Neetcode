class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in nums:
            newResult = []
            for j in result:
                copy = list(j)
                copy.append(i)
                newResult.append(copy)
            result.extend(newResult)
        return result