class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1

        num_set = set(nums)

        if not nums:
            return 0

        for num in num_set:
            if num - 1 not in num_set:
                copy = num
                temp_len = 1
                while copy + 1 in num_set:
                    copy += 1
                    temp_len += 1
                    max_len = max(max_len, temp_len)

        return max_len