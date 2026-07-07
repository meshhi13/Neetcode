class Solution:
    def findMin(self, nums: List[int]) -> int:
            l = 0
            r = len(nums) - 1

            while l <= r:
                print(nums[l: r + 1])
                mid = l + (r - l) // 2
                print(nums[mid])

                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1

            return nums[mid]