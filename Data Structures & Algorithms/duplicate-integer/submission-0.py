class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums = []
        for i in nums:
            if i in newNums:
                return True
            else:
                newNums.append(i)

        return False
