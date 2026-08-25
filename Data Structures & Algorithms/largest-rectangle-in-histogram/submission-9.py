class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = collections.deque()

        max_area = 0
        
        for index in range(len(heights)):
            start = index

            while stack and heights[index] < stack[-1][0]:
                height, prev_start = stack.pop()
                max_area = max(max_area, height * (index - prev_start))
                start = prev_start

            stack.append((heights[index], start))

        while stack:
            height, distance = stack.pop()
            max_area = max(max_area, height * (len(heights) - distance))

        return max_area
            