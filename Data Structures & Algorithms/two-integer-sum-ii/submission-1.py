class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while j > i:
            sumQ = numbers[j] + numbers[i]
            if sumQ > target:
                j = j - 1
            if sumQ < target:
                i = i + 1
            if sumQ == target:
                return [i + 1,j + 1]