class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArr = []
        self.currSum = 0
        for i in nums:
            self.currSum += i
            self.prefixArr.append(self.currSum)

        print(self.prefixArr)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixArr[right]
        return self.prefixArr[right] - self.prefixArr[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)