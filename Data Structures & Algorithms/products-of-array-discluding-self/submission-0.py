class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
        su = 1
        su_no_zero = 1
        num_z = 0

        for i in nums:
            if i != 0:
                su_no_zero *= i
            else:
                num_z += 1
            su *= i

        pro = [su] * len(nums)
            
        for i in range(len(pro)):
            if nums[i] != 0:
                pro[i] = pro[i] // nums[i]
            else:
                pro[i] = su_no_zero

        if num_z >= 2:
            return [0] * len(nums)
        return pro
            