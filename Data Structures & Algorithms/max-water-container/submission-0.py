class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxVol = 0
        while i < j:
            maxVol = max(min(heights[i], heights[j]) * (j - i), maxVol)
            if heights[i] < heights[j]:
                i = i + 1
            else: 
                j = j - 1

        return maxVol

        